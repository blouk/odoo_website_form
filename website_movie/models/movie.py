from odoo import fields, models


class Movie(models.Model):
    _name = "movie"
    _description = "Movie Description"
    _order = "create_date desc, id desc"

    name = fields.Char("Movie Name", required=True)
    rate = fields.Integer("Movie Rate", required=True)
    description = fields.Char("Movie Description")
    image = fields.Binary("Image", attachment=True, help="Movie Image")
    actor_ids = fields.Many2many(
        'actor', 'actor_movie_rel', 'actors', ondelete='cascade')
