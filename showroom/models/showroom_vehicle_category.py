from odoo import models,fields

class ShowroomVehicleCategory(models.Model):
    _name = 'showroom.vehicle.category'
    _description = 'showroom vehicle category'

    name = fields.Char(required=True)