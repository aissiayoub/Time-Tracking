# -*- coding: utf-8 -*-
{
    'name': "Time_Tracking",

    'summary': """Ce module est réalisé dans le cadre d'un stage de fin d'études bac+2
        """,

    'description': """Le logiciel de suivi du temps ou Time Tracking est une catégorie de logiciels permettant à ses employés d’enregistrer le temps consacré à des tâches ou à des projets. Le logiciel est utilisé dans de nombreux secteurs, y compris ceux qui emploient des pigistes et des travailleurs horaires. Il est également utilisé par les professionnels qui facturent leurs clients à l’heure.""",

    'author': "AISSI Ayoub",
    'website': "http://www.facebook.com/picrox",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
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
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto-install': False,
}
