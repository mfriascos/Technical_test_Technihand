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
    commit_line_ids = fields.One2many('commit_line',
                                      'commit_id',
                                      string='Commit Line Ids',
                                      copy=True,
                                      readonly=True,
                                      states={'draft': [('readonly', False)]})


    # @api.depends('commit_line_ids')
    # def _compute_commits_last_date(self):