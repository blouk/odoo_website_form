# -*- coding: utf-8 -*-
{
    "name": "Movie",
    "version": "0.1",
    "author": "Odoo",
    "category": "Website",
    "summary": "Movie",
    "description": """
Movie
========================
    """,
    "depends": [
        'website',
    ],
    "data": [
    'security/ir.model.access.csv',
    'data/data.xml',
    'views/backend.xml',
    'views/template.xml',

    ],
    'qweb': [
    ],
    "installable": True,
}
