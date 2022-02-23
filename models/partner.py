from email.policy import default
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean('Instructor', default=False)
    session_id = fields.Many2many('open_academy.session', string='attended sessions')