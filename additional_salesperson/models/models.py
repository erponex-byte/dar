# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Crm(models.Model):
    _inherit = 'crm.lead'
    add_user_ids = fields.Many2many("res.users")


class Crm(models.Model):
    _inherit = 'project.project'

    multi_manager_ids = fields.Many2many(
        'res.users',
        'project_multi_manager_rel',
        'project_id',
        'user_id',
        string='Project Managers'
    )

