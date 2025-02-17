Below is a sample **README.md** file you can include with your custom module. It describes the purpose of the module, how to install it, and how to use it.

---

# Sale Order Tax Switch

This Odoo module automatically switches the default tax on **Sale Order Lines** between **0%** and **15%** based on whether the line is a down payment line or a regular line.

- **Down Payment (Fixed or Percentage)** → **0%** Tax  
- **Regular Invoice** → **15%** Tax  

## How It Works

1. **Down Payment Lines**  
   - In standard Odoo, when you create an invoice from a **Sale Order** and select **Down payment** (fixed or percentage) in the **Create Invoice** wizard, Odoo sets `is_downpayment = True` on those newly-created lines.  
   - This module detects `is_downpayment = True` and applies the **0%** tax.

2. **Regular Lines**  
   - If you select **Regular Invoice** in the wizard or create lines in another way (without `is_downpayment = True`), the module applies the **15%** tax by default.

3. **Onchange Behavior**  
   - If you manually toggle `is_downpayment` on a line, the tax switches automatically to 0% or 15% depending on the new value.

## Prerequisites

- **Odoo** (version matching your environment) with the **Sales** and **Accounting** apps installed.
- A **0%** tax record in Accounting → Configuration → Taxes with:
  - `amount = 0.0`
  - `type_tax_use = 'sale'`
- A **15%** tax record in Accounting → Configuration → Taxes with:
  - `amount = 15.0`
  - `type_tax_use = 'sale'`

## Installation

1. Copy or clone this module (`custom_sale_tax_switch`) into your Odoo add-ons directory.
2. Update your Odoo app list:
   - Go to **Apps** → **Update Apps List** (in debug mode) → **Update**.
3. Locate the **Sale Order Tax Switch** module and click **Install**.

## Usage

1. Create or open a **Sale Order** in Odoo.
2. Click **Create Invoice** (from the sale order):
   - **Down payment (percentage or fixed)**: The generated lines will have `is_downpayment = True`, so the module applies **0%** tax.
   - **Regular Invoice**: The generated lines will have `is_downpayment = False`, so the module applies **15%** tax.
3. (Optional) Manually edit a **Sale Order Line**:
   - If you toggle `is_downpayment` on or off, the tax will change accordingly.

## Customization

- To change the tax rates or domains, edit the `sale_order_line.py` file:
  ```python
  zero_tax = self.env['account.tax'].search([
      ('amount', '=', 0.0),
      ('type_tax_use', '=', 'sale')
  ], limit=1)
  fifteen_tax = self.env['account.tax'].search([
      ('amount', '=', 15.0),
      ('type_tax_use', '=', 'sale')
  ], limit=1)
  ```
  Adjust these searches to match your desired tax amounts or any other search criteria.

## License

This module is provided under the [MIT License](https://opensource.org/licenses/MIT) or the license of your choice. Modify this section to reflect your actual license.