/*
 * partner -   autocomplete.js
 * Description:
 * Author:           darshan
 * Created:          21 Dec. 2019
 * Source:           https://github.com/dartion/partner
 * License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
 *                   Unauthorized copying of this file, via any medium is
 *                   strictly prohibited. Proprietary and confidential
 */

(function($) {
    'use strict';
    var init = function($element, options) {
        var settings = $.extend({
            ajax: {
                data: function(params) {
                    return {
                        term: params.term,
                        page: params.page
                    };
                }
            }
        }, options);
        $element.select2(settings);
    };

    $.fn.djangoAdminSelect2 = function(options) {
        var settings = $.extend({}, options);
        $.each(this, function(i, element) {
            var $element = $(element);
            init($element, settings);
        });
        return this;
    };

    $(function() {
        // Initialize all autocomplete widgets except the one in the template
        // form used when a new formset is added.
        $('.admin-autocomplete').not('[name*=__prefix__]').djangoAdminSelect2();
    });

    $(document).on('formset:added', (function() {
        return function(event, $newFormset) {
            return $newFormset.find('.admin-autocomplete').djangoAdminSelect2();
        };
    })(this));
}(django.jQuery));
