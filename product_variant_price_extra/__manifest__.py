# -*- coding: utf-8 -*-
# Copyright 2019 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    'name': "Product Variant Price Extra",
    'summary': """
		This module allows to add extra price to the variant additional to attribute price.
        """,
    'version': '12.0.1.0.0',
    'category': 'Warehouse',
    'website': "http://sodexis.com/",
    'author': "Sodexis, Inc <dev@sodexis.com>",
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'depends': [
                'product',
    ],
    'data': [
        'views/product_view.xml',
    ],
}
