# -*- coding: utf-8 -*-
# © 2017 Pedro Gómez <pegomez@elnogal.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    company_registry = fields.Char(size=256)
