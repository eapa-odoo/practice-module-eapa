from odoo import fields, models

class ShowroomVehicle(models.Model):
    _name = 'showroom.vehicle'
    _description = 'showroom vehicle'
    _rec_name = 'veh_company'

    veh_company = fields.Char(required=True, string='Company')
    veh_description = fields.Char(string='Description')
    veh_cost = fields.Integer(string='Cost')
    veh_model_id = fields.Many2one('showroom.vehicle.model',required=True, string='Model')
    veh_type_id = fields.Many2one('showroom.vehicle.type',required=True)
    veh_image = fields.Image()

    veh_model_year = fields.Integer()
    veh_transmission = fields.Selection(
        selection=[('M','Manual'),('A','Automatic')]
    )

    veh_horsepower = fields.Integer()
    veh_power = fields.Integer()
    veh_fuel_type = fields.Selection(
        selection=[('diesel','Diesel'),
                   ('gasoline','Gasoline'),
                   ('full hybrid','Full Hybrid'),
                   ('plug-in hybrid diesel','Plug-in Hybrid Diesel'),
                   ('plug-in hybrid gasoline','Plug-in Hybrid Gasoline'),
                   ('cng','CNG'),
                   ('lpg','LPG'),
                   ('electric','Electric')]
    )
    veh_emissions = fields.Float()

