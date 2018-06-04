#-*- coding: utf-8 -*-

from odoo import models, fields, api
import urllib2
import json
import xmlrpclib
from odoo.exceptions import UserError



class marketplace__integration(models.Model):
	_name = 'marketplace__integration.order'
	# _inherit = 'pos.order'

    
    
	no_invoice = fields.Char(string='Nomor Invoice', required=True)
	customer = fields.Char(string='Customer', )
	tgl_pesan = fields.Date(string='Tanggal Pesan')
	market = fields.Char(string='Marketplace')
	total = fields.Char(string='Total')
	alamat = fields.Char(string='Alamat')
	state = fields.Selection([
		('proses', 'Proses'),
		('selesai', 'Selesai'),
		('rejected', 'Rejected'),
		], default='proses')

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

# class ProductTemplate(models.Model):
#     _inherit = 'product.template'

#     available_in_pos = fields.Boolean(string='Available in the Point of Sale', help='Check if you want this product to appear in the Point of Sale', default=True)
#     to_weight = fields.Boolean(string='To Weigh With Scale', help="Check if the product should be weighted using the hardware scale integration")
#     pos_categ_id = fields.Many2one(
#         'pos.category', string='Point of Sale Category',
#         help="Those categories are used to group similar products for point of sale.")

#     @api.multi
#     def unlink(self):
#         product_ctx = dict(self.env.context or {}, active_test=False)
#         if self.with_context(product_ctx).search_count([('id', 'in', self.ids), ('available_in_pos', '=', True)]):
#             if self.env['pos.session'].search_count([('state', '!=', 'closed')]):
#                 raise UserError(_('You cannot delete a product saleable in point of sale while a session is still opened.'))
#         return super(ProductTemplate, self).unlink()
