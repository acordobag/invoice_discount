# coding: utf-8
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2014 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: Luis Torres (luis_t@vauxoo.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import api, fields, models

class Invoice(models.Model):
    """Inherit from account.invoice to get the amount total without discount and
    the amount total of this, of all invoice lines.
    """
    _inherit = 'account.invoice'

    discount_porcentage = fields.Float(string='Descuento(%)')    
    discount = fields.Float(
        store=True, string='Descuento',
        compute='_get_discount')

    @api.onchange('discount_porcentage')
    def _set_global_discount(self):
        for line in self.invoice_line_ids:
            line.discount=self.discount_porcentage

    def _get_discount(self):
        temp=20
        for line in invoice_line_ids:
            sumated = line.quantity*line.price_unit-line.price_subtotal
            temp += sumated

        self.discount=temp


