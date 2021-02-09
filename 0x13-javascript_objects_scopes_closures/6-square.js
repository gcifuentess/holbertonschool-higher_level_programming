#!/usr/bin/node
// Add charPrint method to Square class

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let strR = c;
    strR = strR.repeat(this.width) + '\n';
    strR = strR.repeat(this.height);
    console.log(strR.slice(0, -1));
  }
}

module.exports = Square;
