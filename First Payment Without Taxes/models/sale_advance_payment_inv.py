from odoo import api, models

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    def _create_invoices(self, order, so_line, amount):
        """Override to remove all taxes from the *first* invoice of the order."""
        # First, let the standard Odoo logic create the invoice
        invoice = super(SaleAdvancePaymentInv, self)._create_invoices(order, so_line, amount)

        # Check if this newly created invoice is the *only* invoice for that order
        # i.e. no previously posted invoices exist => it's effectively the first invoice
        # Alternatively, you can check len(order.invoice_ids) == 1 or any custom condition
        if len(order.invoice_ids) == 1:
            # Remove all taxes from the lines of this invoice
            for line in invoice.invoice_line_ids:
                # Clearing M2M: set tax_ids to an empty list
                line.tax_ids = [(5, 0, 0)]  # remove all tax relations
        return invoice
