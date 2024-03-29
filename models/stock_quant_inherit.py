# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
#    Autor: Brayhan Andres Jaramillo Castaño
#    Correo: brayhanjaramillo@hotmail.com
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from odoo import api, fields, models, _
import time
from datetime import datetime, timedelta, date
import logging
_logger = logging.getLogger(__name__)
from odoo import modules
from odoo.addons import decimal_precision as dp

class StockQuantInherit(models.Model):
	
	_inherit = 'stock.quant'

	product_barcode = fields.Char(string=u'Código de Barras', related='product_id.barcode', digits=dp.get_precision('Product Unit of Measure'))
	product_standard_price = fields.Float(string=u'Costo Producto', related='product_id.standard_price', digits=dp.get_precision('Product Unit of Measure'))

	def _compute_standard_price(self):
		for x in self:
			x.product_standard_price = x.product_id.product_tmpl_id.standard_price




StockQuantInherit()