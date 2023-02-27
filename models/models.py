# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrPayslip(models.Model):
    _inherit="hr.payslip"

    # Comptable
    move_line_ids = fields.Many2many(string="Ecriture comptable",comodel_name="account.move.line", compute="_get_move_line_ids")

    @api.depends('move_id')
    def _get_move_line_ids(self):
        for record in self:
            record.move_line_ids = record.move_id.line_ids