# -*- coding: utf-8 -*-
# from odoo import http


# class IndexPayrollAccounting(http.Controller):
#     @http.route('/index_payroll_accounting/index_payroll_accounting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/index_payroll_accounting/index_payroll_accounting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('index_payroll_accounting.listing', {
#             'root': '/index_payroll_accounting/index_payroll_accounting',
#             'objects': http.request.env['index_payroll_accounting.index_payroll_accounting'].search([]),
#         })

#     @http.route('/index_payroll_accounting/index_payroll_accounting/objects/<model("index_payroll_accounting.index_payroll_accounting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('index_payroll_accounting.object', {
#             'object': obj
#         })
