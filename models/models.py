# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class index_payroll_accounting(models.Model):
#     _name = 'index_payroll_accounting.index_payroll_accounting'
#     _description = 'index_payroll_accounting.index_payroll_accounting'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
