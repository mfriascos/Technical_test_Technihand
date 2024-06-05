# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Repository(models.Model):
    _name = 'repository'
    _description = 'Managing Source Code Repositories in Odoo'

    name = fields.Char('Name')
    link = fields.Char('Link')
    user = fields.Many2one('res.user')
    state = fields.Selection(
        selection=[('draft', 'Draft'),
                   ('active', 'Active'),
                   ('inactive', 'Inactive'),
                   ('cancelled', 'Cancelled')],
        string='Status',
        copy=False,
        default='draft',
        help="When an repo is created, the status is 'Draft'.\n"
        "If the repo is confirmed, the status goes in 'Active'.\n"
        "The 'Inactive' status can be set if the repo is not confirmed.\n"
        "By cancelling an repo, it's possible manually updating")
    commits_last_date = fields.Char(
        'Commits Last Date', compute='_compute_commits_last_date')
    commits_contributor = fields.Many2one('res.partner',
                                          string='count_commits', compute='_compute_commits_contributor')
    commit_line_ids = fields.One2many('commits',
                                      'repository_id',
                                      string='Commit Line Ids',
                                      copy=True,
                                      readonly=True,
                                      states={'draft': [('readonly', False)]})


    @api.depends('commit_line_ids.date')
    def _compute_commits_last_date(self):
        for record in self:
            last_commit = record.commit_line_ids.sorted('date', reverse=True)[:1]
            record.commits_last_date = last_commit.date if last_commit else 'N/A'

    @api.depends('commit_line_ids.partner_id')
    def _compute_commits_contributor(self):
        for record in self:
            top_contributor = record.commit_line_ids.mapped('partner_id')[:1]
            record.commits_contributor = top_contributor.id if top_contributor else False

    def action_active(self):
        self.state = 'active'

    def action_inactive(self):
        self.state = 'inactive'

    def action_cancel(self):
        self.state = 'cancelled'