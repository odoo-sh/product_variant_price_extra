# -*- coding: utf-8 -*-
# Copyright 2019 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import models, fields, api


class Product(models.Model):
    _inherit = 'product.product'

    variant_price_extra = fields.Float('Variant Extra Price', digits='Product Price',
         help="Extra price of the variant additional to attribute prices.")

    @api.depends('list_price', 'price_extra', 'variant_price_extra')
    def _compute_product_lst_price(self):
        super(Product, self)._compute_product_lst_price()
        
        to_uom = None
        if 'uom' in self._context:
            to_uom = self.env['uom.uom'].browse([self._context['uom']])

        for product in self:
            if to_uom:
                list_price = product.uom_id._compute_price(product.list_price, to_uom)
            else:
                list_price = product.list_price
            product.lst_price = list_price + product.price_extra + product.variant_price_extra
            
    def _set_product_lst_price(self):
        super(Product, self)._set_product_lst_price()
        for product in self:
            value = product.list_price
            value -= (product.price_extra + product.variant_price_extra)
            product.write({'list_price': value})
