#!/usr/bin/node
// Define a Rectangle class
class Rectangle {
  // Constructor method to initialize the rectangle with width and height
  constructor (w, h) {
    // Check if both width and height are positive integers
    if (w >= 1 && h >= 1) {
      this.width = w; // Initialize the width property
      this.height = h; // Initialize the height property
    }
    // If not, the instance remains uninitialized (empty object)
  }

  // Method to print the rectangle using the character 'X'
  print () {
    // Check if the rectangle has valid dimensions
    if (this.width && this.height) {
      // Loop through the height of the rectangle
      for (let i = 0; i < this.height; i++) {
        // Print a line of 'X' characters with the length of the width
        console.log('X'.repeat(this.width));
      }
    }
  }

  // Method to swap the width and height of the rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width]; // Swap width and height
  }

  // Method to double the dimensions of the rectangle
  double () {
    this.width *= 2; // Double the width
    this.height *= 2; // Double the height
  }
}

// Export the Rectangle class as a module
module.exports = Rectangle;
