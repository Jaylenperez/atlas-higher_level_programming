#!/usr/bin/node

// Import the 'request' module to handle HTTP requests
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API with the given movie ID
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    // Print the error object if an error occurred
    console.error(error);
  } else {
    // Parse the response body as JSON
    const data = JSON.parse(body);
    // Print the title of the movie
    console.log(data.title);
  }
});
