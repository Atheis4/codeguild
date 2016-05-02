"use strict";

function getInt () {
  return $("#int-input").val();
}

function intToDiceNumber () {
  var int = parseInt(getInt());
  return int;
}

$("form").on("submit", function (event) {
  event.preventDefault();
})

function getRandomInt (min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

function createDiceArray (numberOfDice) {
  var diceArray = [];
  for (var i = 0; i < numberOfDice; i += 1) {
    diceArray.push(getRandomInt(1, 7));
  }
  return diceArray;
}

visualizeDice(createDiceArray(intToDiceNumber()));
