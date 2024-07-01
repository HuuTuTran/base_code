from odoo import models, fields

class subjects(models.Model):
    _name = 'school_management.subjects'
    name = fields.Char(string="Name", required=True)
    no_credits = fields.Integer(min=1, max = 5)
    is_required = fields.Boolean()