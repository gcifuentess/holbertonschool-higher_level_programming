#!/usr/bin/node
// Add rotate and double method to Rectangle class
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

  rotate () {
    let rotate = 0;
    rotate = this.width;
    this.width = this.height;
    this.height = rotate;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
