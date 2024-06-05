# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
from collections import Counter


class Repository(models.Model):
    _name = 'repository'
    _description = 'Managing Source Code Repositories in Odoo'

    name = fields.Char('Name', required=True)
    link = fields.Char('Link')
    user_id = fields.Many2one('res.users', string='User')
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
                        record.commits_last_date = f"The last commit was since {hours} hours"
                    else:
                        days = time_diff.days
                        record.commits_last_date = f"The last commit was since {days} days"
                else:
                    record.commits_last_date = 'N/A'
            else:
                record.commits_last_date = 'N/A'

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

    def action_draft(self):
        self.state = 'draft'

    def action_active(self):
        self.state = 'active'

    def action_inactive(self):
        self.state = 'inactive'

    def action_cancel(self):
        self.state = 'cancelled'
