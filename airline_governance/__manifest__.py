# -*- coding: utf-8 -*-
{
    'name' : 'Airlines',
    'author': "Ravi Bhingradiya",
    'depends': ['mail'],
    'data' : [
            'security/ir.model.access.csv',
            'views/airline_menus.xml',
            'views/airline_airport_view.xml',
            'views/airline_view.xml',
            'views/airline_passenger_view.xml',
            'views/airline_crew_view.xml',
    ],

    'demo' : [ 
            'data/airport_demo_data.xml',
            'data/airline_demo_data.xml',
            'data/passenger_demo_data.xml',
            'data/crew_demo_data.xml',
    ],
    'application' : True,
    'installable': True,

}