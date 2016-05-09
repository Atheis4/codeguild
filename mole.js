'use strict';

// 1. INPUT FUNCTIONS
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

// 2. TRANSFORMATION FUNCTIONS


// 3. CREATE FUNCTIONS
function createHoleImgEl() {
  var holeImgEl = $('<img>').attr(
    'src', 'img/whackmolehole.png'
  );
  return holeImgEl;
}

function createHoleDivEl() {
  var holeDivEl = $('<div></div>').attr(
    'class', 'hole'
  );
  return holeDivEl;
}

function appendHoleImgToHoleDiv() {
  var holeImgEl = createHoleImgEl();
  var holeDivEl = createHoleDivEl();
  holeDivEl.append(holeImgEl);
  return holeDivEl;
}

function appendHoleDivToBoard(holeDivEl) {
  var gameBoardEl = $('#gameboard');
  gameBoardEl.append(holeDivEl);
}

function createScoreSpanEl(score) {
  var scoreSpanEl = $('<span></span>').text(
    'You have brutally murdered ' + score + ' moles. Great job!');
  return scoreSpanEl;
}

// function createScoreH2El() {
//   var scoreH2El = $('h2');
//   return scoreH2El;
// }
//
// function appendScoreSpanElToH2El(score) {
//   var scoreSpanEl = createScoreSpanEl(score);
//   var scoreH2El = createScoreH2El();
//   $(scoreH2El).append(scoreSpanEl);
// }
//
// function appendH2ElToHeaderEl(score) {
//   var scoreH2El = appendScoreSpanElToH2El(score);
//   $('header').append(scoreH2El);
// }

// 4. MODIFY FUNCTIONS
function chooseRandHoleImgEl() {
  var randHoleDivEl = $('div > img')[randomInt(0, 20)];
  return randHoleDivEl;
}

function changeHoleImgElToMoleImgEl() {
  var randHoleImgEl = chooseRandHoleImgEl();
  $(randHoleImgEl).attr('src', 'img/mole.png');
}

// 5. MAIN FUNCTIONS
function buildGameBoard() {
  var holeDivEl = appendHoleImgToHoleDiv();
  appendHoleDivToBoard(holeDivEl);
}

// 6. REGISTER FUNCTIONS
function registerInitialEventHandlers() {
  var score = 0;
  for (var i = 0; i < 20; i++) {
    buildGameBoard();
  }
  window.setInterval(changeHoleImgElToMoleImgEl, 1000);
  $('img').on('click', function(e) {
    $(e.target).attr('src', 'img/whackmolehole.png');
    score += 1;
    appendH2ElToHeaderEl(score);
  });
}

$(document).ready(registerInitialEventHandlers);
