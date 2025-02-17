from odoo import models, fields, api
from odoo.exceptions import ValidationError


class POSOrderReport(models.Model):
    _inherit = 'report.pos.order'

    @api.constrains('pos_order_id', 'date_order', 'session_id')
    def _check_duplicate_orders(self):
        for record in self:
            duplicate_orders = self.env['report.pos.order'].search([
                ('pos_order_id', '=', record.pos_order_id.id),
                ('date_order', '=', record.date_order),
                ('session_id', '=', record.session_id),
                ('id', '!=', record.id)  # Exclude the current record
            ])
            if duplicate_orders:
                raise ValidationError('Duplicate POS order detected in Order Analysis Report!')
