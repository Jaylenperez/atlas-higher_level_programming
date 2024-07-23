#!/usr/bin/node
// Import the Rectangle class from the '5-square' module
const Rectangle = require('./5-square');

// Define a Square class that extends the Rectangle class
class Square extends Rectangle {
  // Constructor method to initialize the square with a given size
  constructor (size) {
    // Call the parent class's constructor with the size for both width and height
    super(size, size);
  }

  // Method to print the square using a specified character
  charPrint (c) {
    // If no character is provided, default to 'X'
    if (c === undefined) {
      c = 'X';
    }
    // Loop through the height of the square
    for (let i = 0; i < this.height; i++) {
      // Print a line of the specified character with the length of the width
      console.log(c.repeat(this.width));
    }
  }
}

// Export the Square class as a module
module.exports = Square;
