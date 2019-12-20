/*
 * partner -   cancel.js
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
    $(function() {
        $('.cancel-link').on('click', function(e) {
            e.preventDefault();
            if (window.location.search.indexOf('&_popup=1') === -1) {
                window.history.back();  // Go back if not a popup.
            } else {
                window.close(); // Otherwise, close the popup.
            }
        });
    });
})(django.jQuery);
