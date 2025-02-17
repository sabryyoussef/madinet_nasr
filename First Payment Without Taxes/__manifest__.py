
{
    'name': 'First Payment Without Taxes',
    'version': '16.0.1.0.0',
    'category': 'Sales/Accounting',
    'summary': 'Automatically removes taxes from the first down payment invoice.',
    'description': """
This module overrides the standard down payment wizard (sale.advance.payment.inv)
to remove taxes from the first invoice created for a Sales Order.
It is especially useful in scenarios where the initial deposit is tax-exempt.
""",
    'author': 'Sabry',
    'website': 'https://yourcompany.com',
    'license': 'AGPL-3',
    'depends': ['sale', 'sale_management', 'account'],
    'data': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
