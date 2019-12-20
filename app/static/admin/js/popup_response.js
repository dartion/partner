/*
 * partner -   popup_response.js
 * Description:
 * Author:           darshan
 * Created:          21 Dec. 2019
 * Source:           https://github.com/dartion/partner
 * License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
 *                   Unauthorized copying of this file, via any medium is
 *                   strictly prohibited. Proprietary and confidential
 */

/*global opener */
(function() {
    'use strict';
    var initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch(initData.action) {
    case 'change':
        opener.dismissChangeRelatedObjectPopup(window, initData.value, initData.obj, initData.new_value);
        break;
    case 'delete':
        opener.dismissDeleteRelatedObjectPopup(window, initData.value);
        break;
    default:
        opener.dismissAddRelatedObjectPopup(window, initData.value, initData.obj);
        break;
    }
})();
