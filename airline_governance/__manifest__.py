# -*- coding: utf-8 -*-
{
    'name' : 'Airlines',
    'author': "Ravi Bhingradiya",
    'data' : [
            'security/ir.model.access.csv',
            'views/airline_model_view.xml',
            'views/airport_model_view.xml',
            'views/passenger_model_view.xml',
            'views/airline_menus.xml',
    ],

    'demo' : [ 
            'data/airline_demo_data.xml',
            'data/passenger_demo_data.xml',
            'data/airport_demo_data.xml',
    ],
    'application' : True,
    'installable': True,

}