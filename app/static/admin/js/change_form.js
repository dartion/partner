/*
 * partner -   change_form.js
 * Description:
 * Author:           darshan
 * Created:          21 Dec. 2019
 * Source:           https://github.com/dartion/partner
 * License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
 *                   Unauthorized copying of this file, via any medium is
 *                   strictly prohibited. Proprietary and confidential
 */

/*global showAddAnotherPopup, showRelatedObjectLookupPopup showRelatedObjectPopup updateRelatedObjectLinks*/

(function($) {
    'use strict';
    $(document).ready(function() {
        var modelName = $('#django-admin-form-add-constants').data('modelName');
        $('body').on('click', '.add-another', function(e) {
            e.preventDefault();
            var event = $.Event('django:add-another-related');
            $(this).trigger(event);
            if (!event.isDefaultPrevented()) {
                showAddAnotherPopup(this);
            }
        });

        if (modelName) {
            $('form#' + modelName + '_form :input:visible:enabled:first').focus();
        }
    });
})(django.jQuery);
