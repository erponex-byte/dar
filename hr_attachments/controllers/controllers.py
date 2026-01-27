# -*- coding: utf-8 -*-
# from odoo import http


# class HrAttachments(http.Controller):
#     @http.route('/hr_attachments/hr_attachments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_attachments/hr_attachments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_attachments.listing', {
#             'root': '/hr_attachments/hr_attachments',
#             'objects': http.request.env['hr_attachments.hr_attachments'].search([]),
#         })

#     @http.route('/hr_attachments/hr_attachments/objects/<model("hr_attachments.hr_attachments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_attachments.object', {
#             'object': obj
#         })

