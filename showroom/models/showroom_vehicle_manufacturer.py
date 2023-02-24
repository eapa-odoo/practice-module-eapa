from odoo import models,fields

class ShowroomVehicleManufacturer(models.Model):
    _name = 'showroom.vehicle.manufacturer'
    _description = 'showroom vehicle manufacturer'

    name = fields.Char(required=True)
    image = fields.Image()