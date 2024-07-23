#!/usr/bin/node
// Import the Rectangle class from the '4-rectangle' module
const Rectangle = require('./4-rectangle');

// Define a Square class that extends the Rectangle class
class Square extends Rectangle {
  // Constructor method to initialize the square with a given size
  constructor (size) {
    // Call the parent class's constructor with the size for both width and height
    super(size, size);
  }
}

// Export the Square class as a module
module.exports = Square;
