from odoo import fields, models

class ShowroomVehicle(models.Model):
    _name = 'showroom.vehicle'
    _description = 'showroom vehicle'
    _rec_name = 'company_id'

    company_id = fields.Many2one('showroom.vehicle.manufacturer', string='Company')
    description = fields.Char(string='Description')
    price = fields.Integer(string='Price')
    image = fields.Image()

    vehicle_id = fields.Many2one('showroom.showroom')
    quantity = fields.Integer()
    
    model_id = fields.Many2one('showroom.vehicle.model', string='Model')
    category_id = fields.Many2one('showroom.vehicle.category',)

    model_year = fields.Integer()
    transmission = fields.Selection(
        selection=[('M','Manual'),('A','Automatic')]
    )

    horsepower = fields.Integer()
    power = fields.Integer()
    fuel_type = fields.Selection(
        selection=[('diesel','Diesel'),
                   ('gasoline','Gasoline'),
                   ('full hybrid','Full Hybrid'),
                   ('plug-in hybrid diesel','Plug-in Hybrid Diesel'),
                   ('plug-in hybrid gasoline','Plug-in Hybrid Gasoline'),
                   ('cng','CNG'),
                   ('lpg','LPG'),
                   ('electric','Electric')]
    )
    emissions = fields.Float()

    tag_ids = fields.Many2many('showroom.vehicle.tag', string='Tags')

    _sql_constraints = [
        ('check_price','CHECK(price >= 0)','The price cannot be negative.'),
    ]
