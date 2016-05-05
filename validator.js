"use strict";

// 1. INPUT FUNCTIONS
//Get input field value f(x)s
function getName() {
  return $("#name").val();
}

function getBirth() {
  return $("#birth").val();
}

function getPhone() {
  return $("#phone").val()
}

//2. VALIDATION FUNCTIONS
//Validate Name field
function validNameFirstLast(name) {
  var valid = false;
  var nameArray = name.split(" ");
  if (nameArray.length >= 2) {
    valid = true;
  }
  return valid;
}

function validNameCapitals(name) {
  var valid = false;
  var nameArray = name.split(" ");
  var capitalCount = 0
  for (var i = 0; i < nameArray.length; i += 1) {
    if (/^[A-Z]/.test(nameArray[i]) === true) {
      capitalCount += 1;
    }
  }
  if (capitalCount >= nameArray.length) {
    valid = true;
  }
  return valid;
}

function validNameCharType(name) {
  var valid = false;
  var badChar = /[0-9]/;
  if (badChar.test(name) === false) {
    valid = true;
  }
  return valid;
}

//Combined Name Validation f(x)s
function validNameSumFunction(name) {
  var firstLast = validNameFirstLast(name);
  var capitals = validNameCapitals(name);
  var charType = validNameCharType(name);
  return firstLast && capitals && charType;
}

//Validate Birth field
function validBirthDate(birth) {
  var valid = false;
  var birthNumberSyntax = /[0-9]{4}\-[0-9]{2}\-[0-9]{2}/;
  if (birthNumberSyntax.test(birth) === true) {
    valid = true;
  }
  return valid;
}

//Validate Phone field
function validPhoneNumber(phone) {
  var valid = false;
  var phoneNumberSyntax = /[0-9]{3}\-[0-9]{3}\-[0-9]{4}/;
  if (phoneNumberSyntax.test(phone) === true) {
    valid = true;
  }
  return valid;
}

// 3. CREATE FUNCTIONS
//Create success dropdown
function createSuccessMsg() {
  var successText = $("<p></p>").text("Congratulations, all fields validated!")
  var newDiv = $("<div></div>").attr("id", "success");
  $("body").prepend(newDiv);
  $("#success").append(successText);
}

//Create error dropdown
function createErrorMsg() {
  var errorText = $("<p></p>").text("Sorry, something is not right.")
  var newDiv = $("<div></div>").attr("id", "fail");
  $("body").prepend(newDiv);
  $("#fail").append(errorText);
}

// 4. MODIFY FUNCTIONS
//Change the background-color of input boxes if valid
function updateNameBoxColor() {
  $("#name").css("background-color", "lightgreen");
}

function updateBirthBoxColor() {
  $("#birth").css("background-color", "lightgreen");
}

function updatePhoneBoxColor() {
  $("#phone").css("background-color", "lightgreen");
}

// 5. MAIN FUNCTIONS
//Test input fields (on submit), create Success/Error Msg
function getAndTestInputs() {
  var name = getName();
  var birth = getBirth();
  var phone = getPhone();
  var gestaltValid = false;
  if (validNameSumFunction(name) && validBirthDate(birth) && validPhoneNumber(phone)) {
    gestaltValid = true;
  }
  if (gestaltValid === true) {
    createSuccessMsg();
  }
  else {
    createErrorMsg();
  }
}

//Validate name box (during input)
function nameBoxValid() {
  var name = getName();
  if (validNameSumFunction(name) === true) {
    updateNameBoxColor();
  }
  else {
    $("#name").css("background-color", "yellow");
  }
}

//Validate birth box (during input)
function birthBoxValid() {
  var birth = getBirth();
  if (validBirthDate(birth) === true) {
    updateBirthBoxColor();
  }
  else {
    $("#birth").css("background-color", "yellow");
  }
}

//Validate phone box (during input)
function phoneBoxValid() {
  var phone = getPhone();
  if (validPhoneNumber(phone) === true) {
    updatePhoneBoxColor();
  }
  else {
    $("#phone").css("background-color", "yellow");
  }
}

// 6. REGISTER FUNCTIONS
//Event Handlers
function registerInitialEventHandlers() {
  $("form").on("submit", function (event) {
    event.preventDefault();
    getAndTestInputs();
  });
  $("#name").on("input", nameBoxValid);
  $("#birth").on("input", birthBoxValid);
  $("#phone").on("input", phoneBoxValid);
}

$(document).ready(function() {
  registerInitialEventHandlers();
});
