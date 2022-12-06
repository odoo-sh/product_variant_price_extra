# Copyright 2019-2022 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import models, fields, api


class Product(models.Model):
    _inherit = 'product.product'

    variant_price_extra = fields.Float('Variant Extra Price', digits='Product Price',
         help="Extra price of the variant additional to attribute prices.")

    def _compute_product_price_extra(self):
        super(Product, self)._compute_product_price_extra()
        for product in self.filtered(lambda x:x.variant_price_extra):
            product.price_extra = sum(product.product_template_attribute_value_ids.mapped('price_extra')) + product.variant_price_extra
