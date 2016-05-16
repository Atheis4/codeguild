'use strict';

function registerEventListener() {
  $('div.setup').on('click', function(event) {
    $(event.target).siblings().css(
      'visibility', 'visible'
    );
  });
}

$(document).ready(registerEventListener);
