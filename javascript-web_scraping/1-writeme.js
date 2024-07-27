#!/usr/bin/node

// Import the 'fs' module to work with file system
const fs = require('fs');

// Get the file path from the command-line arguments
const filePath = process.argv[2];

// Get the string to write from the command-line arguments
const stringToWrite = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    // Print the error object if an error occurred during writing
    console.error(err);
  }
});
