# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime


class Commits(models.Model):
    _name = 'commits'
    _description = 'Managing Source Code Repositories in Odoo'
    _order = "date_desc"

    repository_id = fields.Many2one(
        'repository', string='Repository', index=True, required=True, ondelete='cascade')
    date = fields.Date(string="Date")
    hash = fields.Char(string="Hash")
    partner_id = fields.Many2one('res.partner', string='Partner')
    message = fields.Text(string="Message")