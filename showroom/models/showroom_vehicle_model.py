from odoo import models,fields

class ShowroomVehicleModel(models.Model):
    _name = 'showroom.vehicle.model'
    _description = 'showroom vehicle model'

    name = fields.Char(required=True, string='Model Name')
    description = fields.Char()
    manufacturer_id = fields.Many2one('showroom.vehicle.manufacturer', required=True)
    category_id = fields.Many2one('showroom.vehicle.category', string='Vehicle Category')
    seat_no = fields.Selection(
        selection=[('2 seats','2 Seats'),('4 seats','4 Seats'),('5 seats','5 Seats'),('7 seats','7 Seats')]
    )
    image = fields.Image()
    door_no = fields.Integer()
    model_year = fields.Integer()
    trailer_hitch = fields.Boolean(readonly=False)
    horsepower = fields.Integer()
    transmission = fields.Selection(
        selection=[('M','Manual'),('A','Automatic')]
    )
    power = fields.Integer()
    fuel_type = fields.Selection(
        selection=[('diesel','Diesel'),
                   ('petrol','Petrol'),
                   ('full hybrid','Full Hybrid'),
                   ('plug-in hybrid diesel','Plug-in Hybrid Diesel'),
                   ('plug-in hybrid gasoline','Plug-in Hybrid Gasoline'),
                   ('cng','CNG'),
                   ('lpg','LPG'),
                   ('electric','Electric')]
    )
    emissions = fields.Float()