odoo.define('Movie', function(require) {
    "use strict";
    var core = require('web.core');
    var Class = require('web.Class');
    var Base = require('web_editor.base');
    var Movie = Class.extend({
        init: function() {
            var self = this;
            this.form = $('.mv-form');
            if (this.form.length > 0) {
                this.form.on('click', '.mv-browse', self.on_click_button_browse);
                this.form.on('change', '.mv-file', self.on_change_file_change);
                this.form.on('click', '.js-mv-submit-post', self.on_click_send_post);
                this.form.on('click', '.js-mv-submit-ajx', self.on_click_send_ajx);

            }

            var edit_btn = $('.js-edit-movie');
            if (edit_btn.length > 0) {
                edit_btn.on('click', self.on_movie_edit);
            }
        },
        on_movie_edit: function(ev) {
            var id = $(this).data('movie-id');
            if(id){
                window.location = '/movie/' + id + '/edit';
            }
        },

        on_click_button_browse: function(ev) {
            $('[type=file]').trigger('click');
        },
        on_change_file_change: function() {
            $(this).parent().find('.form-control').val($(this).val().replace(/C:\\fakepath\\/i, ''));
        },

        on_click_send_post: function(ev) {

        },

        on_click_send_ajx: function(ev) {
            ev.preventDefault();
        }

    });

    Base.ready().then(function() {
        new Movie();
    });
});
