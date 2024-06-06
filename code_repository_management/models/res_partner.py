# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    repository_ids = fields.One2many('repository', 'partner_id', string='Repositories')
