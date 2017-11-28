odoo.define('Movie', function(require) {
    "use strict";
    var core = require('web.core');
    var Class = require('web.Class');
    var Base = require('web_editor.base');
    var MovieForm = Class.extend({
        init: function() {
            var self = this;
            this.form = $('.mv-form');
            if (this.form.length > 0) {
                this.form.on('click', '.mv-browse', self.on_click_button_browse);
                this.form.on('change', '.mv-file', self.on_change_file_change);
            }
        },
        on_click_button_browse: function(ev) {
            $('[type=file]').trigger('click');
        },
        on_change_file_change: function() {
            $(this).parent().find('.form-control').val($(this).val().replace(/C:\\fakepath\\/i, ''));
        },

    });

    Base.ready().then(function() {
        new MovieForm();
    });
});
