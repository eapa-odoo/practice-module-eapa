from odoo import api,models,fields

class ShowroomVehicleManufacturer(models.Model):
    _name = 'showroom.vehicle.manufacturer'
    _description = 'showroom vehicle manufacturer'

    name = fields.Char(required=True)
    image = fields.Image()
    model_count = fields.Integer(compute="_compute_model_count", store=True)
    model_ids = fields.One2many('showroom.vehicle.model', 'manufacturer_id')

    @api.depends('model_ids')
    def _compute_model_count(self):
        for record in self:
            record.model_count = len(record.model_ids)

    def action_manufacturer_model(self):
        self.ensure_one()
        view = {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'showroom.vehicle.model',
            'name': 'Models',
            'domain': [('manufacturer_id', '=', self.id)],
            'context': {'search_default_manufacturer_id.id': self.id, 'default_manufacturer_id.manufacturer_id.id': self.id}
        }
        return view