# -*- coding: utf-8 -*-
# from odoo import http


# class Escuelavela(http.Controller):
#     @http.route('/escuelavela/escuelavela', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escuelavela/escuelavela/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('escuelavela.listing', {
#             'root': '/escuelavela/escuelavela',
#             'objects': http.request.env['escuelavela.escuelavela'].search([]),
#         })

#     @http.route('/escuelavela/escuelavela/objects/<model("escuelavela.escuelavela"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escuelavela.object', {
#             'object': obj
#         })
