from odoo import api, fields, models


class SaleOrder(models.Model):
    # inherit database sale.order
    _inherit = 'sale.order'

    sale_description = fields.Char(string='Sale Description')
