#!/usr/bin/node

// Write a function that returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  let Ocounter = 0;
  for (const element of list) {
    if (element === searchElement) {
      Ocounter++;
    }
  }
  return Ocounter;
};
