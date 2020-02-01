# -*- coding: utf-8 -*-
from odoo import http

# class GeonamesTh(http.Controller):
#     @http.route('/geonames_th/geonames_th/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/geonames_th/geonames_th/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('geonames_th.listing', {
#             'root': '/geonames_th/geonames_th',
#             'objects': http.request.env['geonames_th.geonames_th'].search([]),
#         })

#     @http.route('/geonames_th/geonames_th/objects/<model("geonames_th.geonames_th"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('geonames_th.object', {
#             'object': obj
#         })