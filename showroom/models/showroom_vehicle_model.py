from odoo import models,fields

class ShowroomVehicleModel(models.Model):
    _name = 'showroom.vehicle.model'
    _description = 'showroom vehicle model'

    name = fields.Char(required=True, string='Model Name')
    manufacturer_id = fields.Many2one('showroom.vehicle.manufacturer')
    category_id = fields.Many2one('showroom.vehicle.category')
    