from odoo import models, fields

class Students(models.Model):
    _name = 'school_management.students'
    _description = 'a student information class'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="email")
