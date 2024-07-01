from odoo import models, fields

class attachment(models.Model):
    _name = 'chat_application.attachment'
    
    name = fields.Char(string="name", required=True)
    path = fields.Char(string="path", required=True)
