# -*- coding: utf-8 -*-
# © 2017 Pedro Gómez <pegomez@elnogal.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': "GALIPAT Customizations",
    'version': '8.0.0.0.0',
    'author': 'Pedro Gómez <pegomez@elnogal.com>',
    'category': 'Custom',
    'license': 'AGPL-3',
    'description': """Módulo que contiene customizaiones varias para Galipat""",
    'depends': [
        'base',
        'account_asset',
    ],
    'contributors': [
        "Pedro Gómez <pegomez@elnogal.com>"
    ],
    'data': [
        'views/account_asset_view.xml',
        'views/res_company_view.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True
}
