from odoo import http
from odoo.http import request
import base64
import werkzeug


class MovieController(http.Controller):

    @http.route('/movie/form', auth='public', website=True, csrf=False)
    def movie_form(self, **vals):
        #no check on fields
        form_error = False
        if request.httprequest.method == 'POST':
            movie = request.env['movie']

            record = dict(name=vals['movieName'].strip(), description=vals['movieDescription'].strip())
            if(vals.get('movieImage')):
                record['image'] = base64.encodestring(vals['movieImage'].read())

            try:
                movie.create(record)
            except Exception:
                request.cr.rollback()
                form_error = True
            if not form_error:
                return werkzeug.utils.redirect('/movie/thanks', 302)

        vals['error'] = form_error

        return request.render('website_movie.form', vals)

    @http.route('/movie/thanks', auth='public', website=True, csrf=False)
    def thanks(self):
        return request.render('website_movie.thanks')

    @http.route('/movie/list', auth='public', website=True, csrf=False)
    def list(self):
        movie = request.env['movie']
        movies = movie.search([])
        return request.render('website_movie.list',{'movies':movies})
