'use strict';

function registerEventListener() {
  $('div.setup').on('click', function(event) {
    $(event.target).siblings().css(
      'visibility', 'visible'
    );
  });

  var xhr = new XMLHttpRequest();

  function processRequest() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      alert(response);
    }
  }

  xhr.open('POST', 'jokes/ack.html', true);
  xhr.send();
  xhr.addEventListener('readystatechange', processRequest, false);
}

$(document).ready(registerEventListener);
