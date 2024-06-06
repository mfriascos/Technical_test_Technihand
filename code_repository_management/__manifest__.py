# -*- coding: utf-8 -*-
{
    'name': "Code Repository Management",

    'summary': """
        This application was created in order to present the technical test for Technihand's code repository management.
    """,

    'description': """
        Technical test
    """,

    'author': "Mario Fernando Riascos",
    'email': "marioriascos1201@gmail.com",


    'category': 'Test',
    'version': '0.1',

    'depends': ['base', 'contacts'],
    'external_dependencies': {
        'python': ['requests'],
    },

    'data': [
        'security/ir.model.access.csv',
        'views/repository_views.xml',
    ],

    'installable': True,
    'application': True,
}
