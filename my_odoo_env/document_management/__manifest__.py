{
    'name': 'Dokumentų tvaryklė',
    'version': '1.0',
    'summary': 'Dokumentų valdymas',
    'sequence': 10,
    'description': "Valdykite įvairius dokumentus ir jų informaciją",
    'category': 'Tools',
    'website': 'https://www.įmonė.lt',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/document_management_views.xml',
        'wizards/document_report_wizard_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
