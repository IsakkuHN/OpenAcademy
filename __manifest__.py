# -*- coding: utf-8 -*-
{
    'name': "open_academy",

    'summary': """
        Modulo de prueba para la clase de Ingenieria de Software
        """,

    'description': """
        Modulo de prueba
    """,

    'author': "Nelson Rivera 20161031623",
    'website': "http://www.wigmanit2.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/course.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
