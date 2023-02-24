from odoo import models,fields

class ShowroomShowroom(models.Model):
    _name = 'showroom.showroom'
    _description = 'showroom'

    name = fields.Char()
    description = fields.Char()
    types = fields.Selection(
        string = 'Types', 
        selection = [('brand specific','Brand Specific'),('used dealership','Used Dealership'),('small garage','Small Garage'),('online dealership','Online Dealership')],
        help = 'Choose the type of dealership',
    )
    state = fields.Selection(
        string = 'State', 
        default = 'new',
        selection = [('new','New'),('vehicle arrived','Vehicle Arrived'),('vehicle accepted','Vehicle Accepted'),('sold','Sold'),('canceled','Canceled')],
        help = 'Choose the direction',
        required = True,
        copy = False
    )
    address = fields.Char()
    city = fields.Char()
    email = fields.Char()
    contact_no = fields.Char()
    display_capacity = fields.Integer()
    warehouse_capacity = fields.Integer()

    vehicle_ids = fields.One2many('showroom.vehicle','vehicle_id')