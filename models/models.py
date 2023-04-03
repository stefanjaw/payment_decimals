# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountAbstractPayment(models.AbstractModel):
    _inherit = 'account.payment'
    #amount = fields.Monetary(string='Payment Amount', required=True, digits=(18,7) )
    amount = fields.Float(string='Payment Amount', digits=(18,7), required=True)

class accountPayment(models.Model):
    _inherit = 'account.payment'
    payment_difference = fields.Float(compute='_compute_payment_difference', readonly=True, digits=(18,7))
