#!/usr/bin/node
// computes and prints a factorial
let num1 = parseInt(process.argv[2]);
if (!num1) {
  num1 = 1;
}
console.log(factorial(num1));

function factorial (num) {
  if (num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
