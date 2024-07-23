#!/usr/bin/node
// Define class named Rectangle
class Rectangle {
  // Constructor method that gets called when a new instance of Rectangle is created
  constructor (w, h) {
    // Check if both width (w) and height (h) are greater than or equal to 1
    if (w >= 1 && h >= 1) {
      // If the condition is true, set the instance attributes width and height
      this.width = w;
      this.height = h;
    }
    // If either w or h is less than 1, do nothing, leaving the instance without width and height properties
  }
}

// Export the Rectangle class so it can be imported and used in other JavaScript files.
module.exports = Rectangle;
