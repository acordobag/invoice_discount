# -*- coding: utf-8 -*-
{
    'name': "Invoice Discount",

    'summary': """Invoice Discount Costa rica""",

    'description': """

    """,

    'author': "Adrian Cordoba",
    'website': "http://www.yourcompany.com",

    'category': 'account_invoices',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'views/account_invoice_inherited.xml'
    ]
}