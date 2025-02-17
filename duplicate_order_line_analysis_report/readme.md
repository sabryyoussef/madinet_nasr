# POS Order Analysis Fix

## Overview
This module prevents duplicate records in the Odoo **Point of Sale (PoS) Order Analysis Report** and provides a method to clean existing duplicates.

## Features
- **Prevents future duplicates** when creating PoS orders.
- **Provides a script to remove existing duplicates** from the database.
- **Ensures accurate sales reporting** by eliminating double-counting.

## Installation
1. Copy the module to your Odoo addons directory:
   ```bash
   cd /your_odoo_addons_path/
   git clone https://github.com/your-repo/pos_order_analysis_fix.git
   ```
2. Restart Odoo:
   ```bash
   sudo systemctl restart odoo
   ```
3. Install the module from **Apps → Update Apps List** → Search for "POS Order Analysis Fix" → Install.

## Usage
### Preventing Future Duplicates
The module automatically prevents duplicates in the **Order Analysis Report** by checking for existing orders with the same `pos_reference` and `session_id`.

### Removing Existing Duplicates
To clean up old duplicates, run the following command in the Odoo shell:
```bash
$ sudo odoo shell -d your_database_name
```
Then execute:
```python
env['pos.order'].remove_duplicate_orders()
```
This will remove all duplicate PoS orders while keeping only one valid entry per transaction.

## Author
- **Sabry Youssef**

## License
This module is licensed under the **Odoo Community License**.

## Contributions
Pull requests are welcome. Please ensure your code follows Odoo’s development guidelines.

## Contact
For support, please contact **Sabry Youssef**.

