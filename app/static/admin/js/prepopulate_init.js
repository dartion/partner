/*
 * partner -   prepopulate_init.js
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
    var fields = $('#django-admin-prepopulated-fields-constants').data('prepopulatedFields');
    $.each(fields, function(index, field) {
        $('.empty-form .form-row .field-' + field.name + ', .empty-form.form-row .field-' + field.name).addClass('prepopulated_field');
        $(field.id).data('dependency_list', field.dependency_list).prepopulate(
            field.dependency_ids, field.maxLength, field.allowUnicode
        );
    });
})(django.jQuery);
