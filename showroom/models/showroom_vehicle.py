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

    veh_model_year = fields.Integer()
    veh_transmission = fields.Selection([('M','Manual'),('A','Automatic')])