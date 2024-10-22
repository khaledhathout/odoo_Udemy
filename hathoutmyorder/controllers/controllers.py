# -*- coding: utf-8 -*-
# from odoo import http


# class Hathoutmyorder(http.Controller):
#     @http.route('/hathoutmyorder/hathoutmyorder', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hathoutmyorder/hathoutmyorder/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hathoutmyorder.listing', {
#             'root': '/hathoutmyorder/hathoutmyorder',
#             'objects': http.request.env['hathoutmyorder.hathoutmyorder'].search([]),
#         })

#     @http.route('/hathoutmyorder/hathoutmyorder/objects/<model("hathoutmyorder.hathoutmyorder"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hathoutmyorder.object', {
#             'object': obj
#         })
