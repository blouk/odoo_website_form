from odoo import fields, models
class Movie(models.Model):
    _name = "movie"
    _description = "Movie Description"
    _order = "create_date desc, id desc"

    name = fields.Char("Movie Name", required=True)
    description = fields.Html("Movie Description")
    image = fields.Binary("Image", attachment=True, help="Movie Image")
