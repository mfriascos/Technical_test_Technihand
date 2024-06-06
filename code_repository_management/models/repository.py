from odoo import models, fields, api
from datetime import datetime, timedelta
from collections import Counter
import requests


class Repository(models.Model):
    _name = 'repository'
    _description = 'Managing Source Code Repositories in Odoo'

    name = fields.Char('Name', required=True)
    link = fields.Char('Link')
    partner_id = fields.Many2one('res.partner', string='Partner')
    state = fields.Selection(
        selection=[('draft', 'Draft'),
                   ('active', 'Active'),
                   ('inactive', 'Inactive'),
                   ('cancelled', 'Cancelled')],
        string='Status',
        copy=False,
        default='draft',
        help="When a repository is created, the status is 'Draft'.\n"
             "If the repository is confirmed, the status goes to 'Active'.\n"
             "The 'Inactive' status can be set if the repository is not confirmed.\n"
             "By cancelling a repository, it's possible manually updating")
    commits_last_date = fields.Char(
        'Commits Last Date', compute='_compute_commits_last_date')
    commits_contributor = fields.Many2one(
        'res.partner', string='Commits Contributor', compute='_compute_commits_contributor')
    commit_line_ids = fields.One2many('commits', 'repository_id', string='Commit Line Ids',
                                      copy=True, readonly=True, states={'draft': [('readonly', False)]})
    last_commit_url = fields.Char(
        string="Last Commit URL", compute='_compute_last_commit_url', store=True)
    check_time = fields.Boolean("Check time", default=False)

    @api.depends('commit_line_ids.date')
    def _compute_commits_last_date(self):
        for record in self:
            if record.commit_line_ids:
                last_commit = max(record.commit_line_ids.mapped('date'))
                if last_commit:
                    last_commit_datetime = fields.Datetime.from_string(
                        last_commit)
                    last_commit_datetime = fields.Datetime.context_timestamp(
                        record, last_commit_datetime)
                    current_datetime = fields.Datetime.context_timestamp(
                        record, fields.Datetime.now())
                    time_diff = current_datetime - last_commit_datetime

                    if time_diff < timedelta(hours=24):
                        hours = time_diff.seconds // 3600
                        record.commits_last_date = f"The last commit was {hours} hours ago"
                        record.check_time = True
                    else:
                        days = time_diff.days
                        record.commits_last_date = f"The last commit was {days} days ago"
                        record.check_time = False
                else:
                    record.commits_last_date = 'N/A'
                    record.check_time = False
            else:
                record.commits_last_date = 'N/A'
                record.check_time = False

    @api.depends('commit_line_ids.partner_id')
    def _compute_commits_contributor(self):
        for record in self:
            if record.commit_line_ids:
                contributors = [
                    line.partner_id for line in record.commit_line_ids if line.partner_id]
                if contributors:
                    find_contributor = Counter(contributors)
                    top_contributor = find_contributor.most_common(1)
                    record.commits_contributor = top_contributor[0][0] if top_contributor else False
                else:
                    record.commits_contributor = False
            else:
                record.commits_contributor = False

    @api.depends('link')
    def _compute_last_commit_url(self):
        for record in self:
            if record.link:
                owner_repo = record.link.replace("https://github.com/", "")
                api_url = f"https://api.github.com/repos/{owner_repo}/commits"
                try:
                    response = requests.get(api_url)
                    response.raise_for_status()
                    commits_data = response.json()
                    if commits_data:
                        last_commit = commits_data[0]
                        record.last_commit_url = f"https://github.com/{owner_repo}/commit/{last_commit.get('sha')}"
                    else:
                        record.last_commit_url = False
                except requests.exceptions.RequestException:
                    record.last_commit_url = False
            else:
                record.last_commit_url = False

    def action_open_commit(self):
        self.ensure_one()
        if self.last_commit_url:
            return {
                'type': 'ir.actions.act_url',
                'url': self.last_commit_url,
                'target': 'new',
            }

    def action_draft(self):
        self.state = 'draft'

    def action_active(self):
        self.state = 'active'

    def action_inactive(self):
        self.state = 'inactive'

    def action_cancel(self):
        self.state = 'cancelled'
