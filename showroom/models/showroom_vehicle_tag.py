from odoo import models,fields

class ShowroomVehicleTag(models.Model):
    _name = 'showroom.vehicle.tag'
    _description = 'showroom vehicle tag'

    name = fields.Char(required=True)
