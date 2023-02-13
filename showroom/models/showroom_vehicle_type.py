from odoo import models,fields

class ShowroomVehicleType(models.Model):
    _name = "showroom.vehicle.type"
    _description = "showroom vehicle type"
    _rec_name = "veh_type"

    veh_type = fields.Char(required=True)