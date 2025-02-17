# First Payment Without Taxes

This module customizes Odoo's down payment wizard so that the **first invoice** created from a Sales Order is generated **without any taxes**. This is particularly useful in scenarios where an initial deposit or down payment is tax-exempt (for example, when a down payment is considered a guarantee rather than a payment for services).

## Features

- **Automatic Tax Removal:** The module overrides the default behavior of the down payment wizard to remove tax lines on the first invoice.
- **Seamless Integration:** Works within Odoo's standard Sales Order and invoicing workflows.
- **Compliance:** Useful for businesses operating in regions where down payments or deposits are exempt from taxation.

## Use Case Scenario: Construction Company Down Payment

### Background

A construction company collects an initial deposit before commencing work on a project. According to local tax regulations, this down payment is considered a deposit and is **exempt from VAT**. However, when the project work begins and the remaining balance is invoiced, normal tax rules apply.

### Standard Odoo Behavior

1. **Sales Order Creation:**  
   A Sales Order is created for a project valued at $100,000, with VAT applied to the service lines.
2. **Down Payment Invoice:**  
   When processing a 20% down payment (i.e., $20,000), the default behavior would create an invoice that includes VAT based on the Sales Order's tax settings.
3. **Final Invoice:**  
   The remaining balance invoiced later will include the applicable VAT.

### Behavior with This Module

1. **Sales Order Confirmation:**  
   The sales team creates and confirms the Sales Order as usual.
2. **Down Payment Processing:**  
   - The user selects **Create Invoice** → chooses **Down Payment**.
   - The module intercepts the invoice creation process.
   - It checks if the newly created invoice is the first for that Sales Order.
   - **Result:** All tax lines are removed, ensuring the down payment invoice is issued without any taxes.
3. **Final Invoicing:**  
   When the remaining amount is invoiced later, the standard tax rules are applied, and the invoice includes the appropriate taxes.

## Installation

1. **Copy the Module Folder:**  
   Place the `first_payment_no_tax` folder into your Odoo `addons` directory.
2. **Update Apps List:**  
   Restart Odoo and update the apps list.
3. **Install the Module:**  
   Locate "First Payment Without Taxes" in the Apps menu and install it.
4. **Process Sales Orders as Usual:**  
   The module will automatically remove taxes from the first down payment invoice.

## Module Structure

