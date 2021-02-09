#!/usr/bin/node
// Add charPrint method to Square class

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
