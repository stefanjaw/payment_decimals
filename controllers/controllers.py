# -*- coding: utf-8 -*-
from odoo import http

# class PaymentDecimals(http.Controller):
#     @http.route('/payment_decimals/payment_decimals/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payment_decimals/payment_decimals/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payment_decimals.listing', {
#             'root': '/payment_decimals/payment_decimals',
#             'objects': http.request.env['payment_decimals.payment_decimals'].search([]),
#         })

#     @http.route('/payment_decimals/payment_decimals/objects/<model("payment_decimals.payment_decimals"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payment_decimals.object', {
#             'object': obj
#         })