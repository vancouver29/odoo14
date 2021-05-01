# -*- coding: utf-8 -*-
# {
#     'name': "openacademy1",
#
#     'summary': """
#         Short (1 phrase/line) summary of the module's purpose, used as
#         subtitle on modules listing or apps.openerp.com""",
#
#     'description': """
#         Long description of module's purpose
#     """,
#
#     'author': "My Company",
#     'website': "http://www.yourcompany.com",
#
#     # Categories can be used to filter modules in modules listing
#     # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
#     # for the full list
#     'category': 'Uncategorized',
#     'version': '0.1',
#
#     # any module necessary for this one to work correctly
#     'depends': ['base'],
#
#     # always loaded
#     'data': [
#         # 'security/ir.model.access.csv',
#         'views/views.xml',
#         'views/templates.xml',
#     ],
#     # only loaded in demonstration mode
#     'demo': [
#         'demo/demo.xml',
#     ],
# }

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Open Academy',
    'version': '1.0',
    'summary': 'Open Academy Software',
    'sequence': -99,
    'description': """Open Academy Software""",
    'category': 'Extra Tools',
    'author': 'vancouver299',
    'maintainer': 'vancouver299',
    'website': 'https://github.com/vancouver29',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'demo/demo.xml'
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml'],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

