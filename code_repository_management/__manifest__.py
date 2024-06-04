# -*- coding: utf-8 -*-
{
    'name': "Repository Code Management",

    'summary': """
        This application was created in order to present the technical test for Technihand's code repository management.""",

    'description': """
        Technical test
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/repository_views.xml',
        'views/commits_views.xml',
    ],
}
