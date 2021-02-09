#!/usr/bin/node
// Add print method to Rectangle class
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    this.print = function () {
      if (w > 0 && h > 0) {
        let strR = 'X';
        strR = strR.repeat(w) + '\n';
        strR = strR.repeat(h);
        console.log(strR.slice(0, strR.length - 1));
      }
    };
  }
}

module.exports = Rectangle;
