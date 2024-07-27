#!/usr/bin/node

// Import the 'fs' module to work with file system
const fs = require('fs');

// Get the file path from the command-line arguments
const filePath = process.argv[2];

// Read the file content in UTF-encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // Print the error object if an error occured
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
