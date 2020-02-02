# -*- coding: utf-8 -*-
{
    'name': "geonames_th",

    'summary': """
        A helper module for setting geonames in Thai.
        """,

    'description': """
        This module does
        - load base_location_geonames_import
        - set geonames.url to use Thai data from my repo.
        - adjust onchange of zip_id to fill Tambol for street2 and Amphor for city.
    """,

    'author': "Poonlap V.",
    'website': "https://github.com/poonlap/geonames_th",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base_location_geonames_import'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/view_config_parameter.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
