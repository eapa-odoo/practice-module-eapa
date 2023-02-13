from odoo import models,fields

class ShowroomVehicleModel(models.Model):
    _name = "showroom.vehicle.model"
    _description = "showroom vehicle model"
    _rec_name = "veh_model"

    veh_model = fields.Char(required=True)