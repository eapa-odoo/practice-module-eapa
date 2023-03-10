{
    'name': 'Showroom',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/showroom_vehicle_views.xml',
        'views/showroom_vehicle_manufacturer_views.xml',
        'views/showroom_vehicle_model_views.xml',
        'views/showroom_vehicle_category_views.xml',
        'views/showroom_vehicle_tag_views.xml',
        'views/showroom_showroom_views.xml',
        'views/showroom_menus.xml',
    ],
    'demo': [
        'demo/showroom_demo.xml',
    ]
}