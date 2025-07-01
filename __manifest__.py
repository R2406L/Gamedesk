# -*- coding: utf-8 -*-
{
    'name': "GameDesk role play",
    'description': "GameDesk role play scheduler",
    'author': "R2406",
    'website': "https://svgun.ru/odoo",
    'category': 'Services',
    'version': '0.0.1',
    'license': 'GPL-3',

    'depends': ['base', 'mail'],

    'auto_install': False,
    'installable': True,
    'application': True,

    'data': [
	'security/groups.xml',
	'security/ir.model.access.csv',

	'views/games.xml',
	'views/engine.xml',
        'views/setting.xml',
	'views/_menu.xml',
    ],
}
