#!/usr/bin/node
// prints the number of arguments already printed and the new argument value
// Output format: <number arguments already printed>: <current argument value>
exports.logMe = function (item) {
  this.count = (this.count || 0) + 1;
  console.log(`${this.count - 1}: ${item}`);
};
