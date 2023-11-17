# -*- coding: utf-8 -*-
# © 2017 Pedro Gómez <pegomez@elnogal.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': "GALIPAT Reports",
    'version': '8.0.0.0.0',
    'author': 'Pedro Gómez <pegomez@elnogal.com>',
    'category': 'Custom',
    'license': 'AGPL-3',
    'description': """Módulo que contiene reportes de Galipat""",
    'depends': [
        'base',
        'report',
    ],
    'contributors': [
        "Pedro Gómez <pegomez@elnogal.com>"
    ],
    'data': [
        'data/report_paperformat.xml',
        'views/layouts_custom.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True
}
