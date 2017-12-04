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

            record = dict(name=vals['movieName'].strip(), description=vals['movieDescription'].strip(),rate=vals['movieRate'])
            if(vals.get('movieImage')):
                record['image'] = base64.encodestring(vals['movieImage'].read())
            try:
                if vals['update'] == '1':
                    movie_id = movie.search([('id','=',vals.get('movie_id'))])
                    movie_id.update(record)
                else:
                    movie.create(record)

            except Exception:
                request.cr.rollback()
                form_error = True
            if not form_error:
                return werkzeug.utils.redirect('/movie/thanks', 302)

        vals['error'] = form_error

        return request.render('website_movie.form', vals)


    @http.route('/movie/<int:movie_id>/edit', auth='public', website=True, csrf=False)
    def detail(self,movie_id):
        error = False
        record = dict()
        movie = request.env['movie']
        movie_id = movie.search([('id','=',movie_id)])
        if movie_id:
            record['movie'] = movie_id
        else:
            error = True
        record['no_movie'] = error
        return request.render('website_movie.detail',record)


    @http.route('/movie/thanks', auth='public', website=True, csrf=False)
    def thanks(self):
        return request.render('website_movie.thanks')

    @http.route('/movie/list', auth='public', website=True, csrf=False)
    def list(self):
        movie = request.env['movie']
        movies = movie.search([])
        return request.render('website_movie.list',{'movies':movies})
