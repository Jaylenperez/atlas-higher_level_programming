#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    // Check if height is not provided or is negative, then set it to undefined.
    this.height = typeof h === 'number' && h > 0 ? h : undefined;
  }
}

module.exports = Rectangle;
