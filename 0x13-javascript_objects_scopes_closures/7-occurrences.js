#!/usr/bin/node
// Returns the number of occurrences in a list:
exports.nbOccurences = function (list, element) {
  let nbOcurr = 0;
  list.forEach(x => {
    if (x === element) {
      nbOcurr += 1;
    }
  });
  return nbOcurr;
};
