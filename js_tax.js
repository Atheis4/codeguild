"use strict";

var grossIncome = 0;

var taxMap = {
  "3350": 0.05,
  "8400": 0.07,
  "125000": 0.09,
  "over": 0.099
};

var arrayTaxMap = function(taxMap) {
  var taxBracketArr = [];
  for (var key in taxMap){
    taxBracketArr.push(key);
  };
  return taxBracketArr;
};

var calcTaxes = function(grossIncome, taxBracketArr) {

  if (grossIncome <= parseInt(taxBracketArr[0])) {
    return taxObligation = grossIncome * taxMap[taxBracketArr[0]];
  }

  if (grossIncome <= parseInt(taxBracketArr[1])) {
    return taxObligation = (parseInt(taxBracketArr[0]) * taxMap[taxBracketArr[0]]) + ((grossIncome - 3350) * taxMap[taxBracketArr[1]]);
  }

  if (grossIncome <= parseInt(taxBracketArr[2])) {
    return taxObligation = (167.5 + 353.5) + ((grossIncome - 8400) * taxMap[taxBracketArr[2]]);
  }

  if (grossIncome > parseInt(taxBracketArr[2])) {
    return taxObligation = (167.5 + 353.5 + 10494) + ((grossIncome - 125000) * taxMap[taxBracketArr[3]]);
  }
};

var taxBracketArr = arrayTaxMap(taxMap);
var taxObligation = calcTaxes(grossIncome, taxBracketArr);

console.log(calcTaxes(50000, taxBracketArr));
console.log(calcTaxes(100000, taxBracketArr));
console.log(calcTaxes(125000, taxBracketArr));
console.log(calcTaxes(125001, taxBracketArr));
