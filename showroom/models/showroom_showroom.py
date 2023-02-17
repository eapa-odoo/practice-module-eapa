from odoo import models,fields

class ShowroomShowroom(models.Model):
    _name = 'showroom.showroom'
    _description = 'showroom'

    name = fields.Char()

