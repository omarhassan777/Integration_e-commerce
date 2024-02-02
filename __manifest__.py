
{
    "name": "Integration Module",
    "summary": "Integration between e-commerce platform and odoo",
    "website": "odoo.com",
    "application": True,
    'sequence': -10,
    "depends": ["mail", 'base'],
    "data": [
        "secuirty/ir.model.access.csv",
        "views/menu.xml",
        "views/product.xml",



    ],


    'license': 'AGPL-3',


}
