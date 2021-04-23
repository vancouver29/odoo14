# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Extra Tools',
    'author': 'vancouver299',
    'maintainer': 'vancouver299',
    'website': 'https://github.com/vancouver29',
    # any module necessary for this one to work correctly
    'depends': [],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
