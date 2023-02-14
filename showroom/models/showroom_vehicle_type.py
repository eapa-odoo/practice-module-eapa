from odoo import models,fields

class ShowroomVehicletype(models.Model):
    _name = 'showroom.vehicle.type'
    _description = 'showroom vehicle type'

    name = fields.Char(required=True)