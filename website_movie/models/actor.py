from odoo import fields, models


class Actor(models.Model):
    _name = "actor"
    _description = "Actor Description"
    name = fields.Char("Actor Name", required=True)
    firstname = fields.Char("Actor Firstname", required=True)
    age = fields.Integer("Actor Age")
