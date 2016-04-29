"use strict";

// Write a f(x) named find_sum_pairs.
// It takes 2 arguments: a list of ints to search and a sum to find.
// Search through list to find all pairs of numbers that would add together to equal the sum.

var find_sum_pairs = function(array, sum) {
  var sumList = [];
  for (var i = 0; i < array.length; i += 1) {
    var number = array[i];
    var difference = sum - number;

    if (array.find(function(i){return (i === difference)})){
      sumList.push([number, difference]);
    };

  };
  if (sumList.find(function(i, j){return (j, i === i, j)})){
    sumList.pop([number, difference]);
  };
  console.log(sumList);
};

find_sum_pairs([-1, 0, 1, 2], 3);
find_sum_pairs([-1, 0, 1, 2], 1);
find_sum_pairs([2, -1, 2], 1);
find_sum_pairs([-1, 1, 2, 2], 3);
