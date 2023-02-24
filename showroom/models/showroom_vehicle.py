from odoo import api,fields, models

class ShowroomVehicle(models.Model):
    _name = 'showroom.vehicle'
    _description = 'showroom vehicle'
    _rec_name = 'company_id'

    company_id = fields.Many2one('showroom.vehicle.manufacturer', string='Company')
    description = fields.Char()
    image = fields.Image(compute='_compute_info',store=True)
    description = fields.Char(string='Description')
    price = fields.Integer(string='Price')
    tag_ids = fields.Many2many('showroom.vehicle.tag', string='Tags')
    model_id = fields.Many2one('showroom.vehicle.model', string='Model', domain="[('manufacturer_id', '=', company_id)]")
    category_name = fields.Char(compute='_compute_info',store=True)
    seat_no = fields.Char(compute='_compute_info', store=True)
    door_no = fields.Char(compute='_compute_info', store=True)
    model_year = fields.Integer(compute='_compute_info', store=True)
    trailer_hitch = fields.Boolean(compute='_compute_info', store=True)
    transmission = fields.Char(compute='_compute_info', store=True)
    horsepower = fields.Integer(compute='_compute_info', store=True)
    power = fields.Integer(compute='_compute_info', store=True)
    fuel_type = fields.Char(compute='_compute_info', store=True)
    emissions = fields.Float(compute='_compute_info', store=True)
    vehicle_id = fields.Many2one('showroom.showroom')

    _sql_constraints = [
        ('check_price','CHECK(price >= 0)','The price cannot be negative.'),
    ]

    @api.depends('model_id')
    def _compute_info(self):
        for record in self:
            record.category_name = record.model_id.category_id.name
            record.image = record.model_id.image
            record.seat_no = record.model_id.seat_no
            record.door_no = record.model_id.door_no
            record.model_year = record.model_id.model_year
            record.trailer_hitch = record.model_id.trailer_hitch
            record.transmission = record.model_id.transmission
            record.horsepower = record.model_id.horsepower
            record.power = record.model_id.power
            record.fuel_type = record.model_id.fuel_type
            record.emissions = record.model_id.emissions
