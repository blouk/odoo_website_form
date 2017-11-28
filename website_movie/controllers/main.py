from odoo import http
from odoo.http import request

class MovieController(http.Controller):
    @http.route('/movie/form', auth='public', website=True, csrf=False)
    def movie_form(self, **vals):
        return request.render('website_movie.form')
