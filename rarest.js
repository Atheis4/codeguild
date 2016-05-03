"use strict";

var namesToAges = {
    "Alyssa": 22,
    "Charley": 25,
    "Dan": 25,
    "Jeff": 20,
    "Kasey": 20,
    "Kim": 20,
    "Morgan": 25,
    "Ryan": 25,
    "Stef": 22
};

var ageCountObj = {};
// begins for loop, iterates over names in namesToAges mapping (obj)
for (var name in namesToAges) {
  // set new var to the age of each person in our namesToAges obj.
  var age = namesToAges[name];
  // if statement: bool asks if age already exists as a key in our new obj... If it does, add one to value.
  if (age in ageCountObj) {
    ageCountObj[age] += 1;
  }
  // else: create new key, value (mapping) pair: key=age, value=1.
  else {
    ageCountObj[age] = 1;
  }
};

// new obj created to map the frequency of each age to the age number
var countAgeObj = {};
// begins the for loop, iterates through the ages in ageCountObj
for (var age in ageCountObj) {
  // sets new variable to the frequency of each age.
  var frequency = ageCountObj[age];
  // maps this frequency to the age completing the key/value swap.
  countAgeObj[frequency] = age;
};

// creates empty array
var sortedArray = [];
// iterates through our list of frequencies in countAgeObj
for (var frequency in countAgeObj) {
  // appends each frequency to our new array
  sortedArray.push(frequency);
};

// sort method/function/thing sorts array from smallest to largest.
sortedArray.sort();
// new var to capture just the least frequent count
var rarestNumber = sortedArray[0];
// var used to call the appropriate age from our countAgeObj, printed to console.
console.log(countAgeObj[rarestNumber]);
