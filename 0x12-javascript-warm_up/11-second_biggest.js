#!/usr/bin/node
// searches the second biggest integer in the list of arguments.
let submax = 0;
let max = 0;
let current = 0;
process.argv.forEach((val, index) => {
  if (index > 1) {
    current = parseInt(val);
    if (max <= current) {
      submax = max;
      max = current;
    } else if (submax <= current) {
      submax = current;
    }
  }
});
console.log(submax);
