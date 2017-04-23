# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
            return [
                {
                    "label": _("Legal Reports France"),
                    "icon": "fa fa-table",
                    "items": [
                                {
                                    "type": "report",
                                    "name": "Fichier des Ecritures Comptables [FEC]",
                                    "doctype": "GL Entry",
                                    "is_query_report": True
                                }
                    ]
                }
            ]
        
