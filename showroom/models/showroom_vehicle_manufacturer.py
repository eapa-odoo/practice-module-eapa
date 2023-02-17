from odoo import models,fields

class ShowroomVehicleManufacturer(models.Model):
    _name = 'showroom.vehicle.manufacturer'
    _description = 'showroom vehicle manufacturer'

    image = fields.Image()
    name = fields.Char(required=True)