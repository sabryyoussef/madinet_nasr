from odoo import models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.model
    def default_get(self, fields_list):
        res = super(SaleOrderLine, self).default_get(fields_list)
        # Set default tax to 0% if tax exists
        zero_tax = self.env['account.tax'].search([
            ('amount', '=', 0.0),
            ('type_tax_use', '=', 'sale')
        ], limit=1)
        if zero_tax:
            res['tax_id'] = [(6, 0, zero_tax.ids)]
        return res

    @api.onchange('product_id')
    def _onchange_product_id(self):
        # Directly set the tax to 0% when a product is added
        zero_tax = self.env['account.tax'].search([
            ('amount', '=', 0.0),
            ('type_tax_use', '=', 'sale')
        ], limit=1)
        if zero_tax:
            self.tax_id = [(6, 0, zero_tax.ids)]
