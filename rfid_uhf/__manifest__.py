# Copyright 2020 Vauxoo
# License AGPL-3 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Control RFID of UHF',
    'summary': '''
    Instance creator for Vauxoo. This is the app.
    ''',
    'author': 'Vauxoo',
    'website': 'https://www.vauxoo.com',
    'license': 'AGPL-3',
    'category': 'Installer',
    'version': '15.0.1.0.0',
    'depends': [
       'base',
    ],
    'test': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/control_rfid.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
