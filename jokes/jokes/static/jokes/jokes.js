'use strict';

function registerEventHandlers() {
  $('div.setup').on('click', function(event) {
    $(event.target).siblings().css(
      'visibility', 'visible'
    );
  });
}

$(document).ready(registerEventHandlers);
