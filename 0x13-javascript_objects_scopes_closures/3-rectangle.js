#!/usr/bin/node
// Add print method to Rectangle class
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      let strR = 'X';
      strR = strR.repeat(this.width) + '\n';
      strR = strR.repeat(this.height);
      console.log(strR.slice(0, -1));
    }
  }
}

module.exports = Rectangle;
