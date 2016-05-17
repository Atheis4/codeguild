'use strict';

// 1. INPUT FUNCTIONS
function getNumber() {
  var inputNumber = $('#int-input').val();
  return Number(inputNumber);
}

// 2. TRANSFORM FUNCTIONS
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

function createSingleDice() {
  var diceValue = randomInt(1, 7);
  return diceValue;
}

function createDiceDiv() {
  var diceDiv = $('<div></div>').attr(
    'class', 'dice value-' + createSingleDice());
  diceDiv.on('click', function() {
    diceDiv.remove();
  });
  return diceDiv;
}

// 3. CREATION FUNCTIONS
function createDiceSetDiv(inputNumber) {
  for (var i = 0; i < inputNumber; i += 1) {
    var diceDiv = createDiceDiv();
    $('#dice-container').append(diceDiv);
  }
}

function createScoreArray() {
  var diceClassArray = [];
  $('div').each(function(i, e) {
    diceClassArray.push(e.className);
  });
  return diceClassArray;
}

function splitScoreArray(diceClassArray) {
  var scoreArray = [];
  for (var i = 0; i < diceClassArray.length; i += 1) {
    var diceValue = diceClassArray[i][-1];
    scoreArray.push(diceValue);
  }
  return scoreArray;
}

// 4. MODIFY FUNCTIONS
function clearRolls() {
  $('#dice-container').empty();
}

// 5. MAIN FUNCTIONS
function getRollInputcreateDiceSetAndDiceDiv() {
  var inputNumber = getNumber();
  createDiceSetDiv(inputNumber);
}

function scoreFunctions() {
  var diceClassArray = createScoreArray();
  var scoreArray = splitScoreArray(diceClassArray);
  return scoreArray;
}

// 6. REGISTER FUNCTIONS
function registerInitialEventHandlers() {
  $('form').on('submit', function(event) {
    event.preventDefault();
    clearRolls();
    getRollInputcreateDiceSetAndDiceDiv();
    scoreFunctions();
  });
}

$(document).ready(registerInitialEventHandlers);
