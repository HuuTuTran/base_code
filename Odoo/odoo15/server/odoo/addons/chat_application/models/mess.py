from odoo import models, fields

class mess(models.Model):
    _inherit = 'mail.channel'
    print('IMPORTED')
    custom_field = fields.Char(string="custom_field")

