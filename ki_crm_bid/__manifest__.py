# -*- coding: utf-8 -*-


{
    'name': "CRM Bid Account",
    'summary': """CRM Bid Account""",
    'description': """CRM Bid Account""",
    'version': "0.5",
    'category': "CRM",
    'author': "Manas Ram satapathy",
    "depends": [
        'crm','portal','ki_crm_portal','website','base'
    ],
    "data": [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/crm_bid_view.xml',
        'views/crm_portal_template.xml',
        'views/crm_lead_view.xml',
        'views/res_users_view.xml'
    ],
    'application': False,
    'installable': True,
}
