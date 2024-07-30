#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  // Write the body to the file with UTF-8 encoding
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(`Error writing to file: ${err}`);
      return;
    }
    // console.log(`Content saved to ${filePath}`);
  });
});
