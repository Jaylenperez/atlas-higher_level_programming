#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');

// Get command line arguments
const argv = process.argv;

// Make an HTTP GET request to the URL provided as the second command line argument
request(argv[2], function (error, response, body) {
  if (error) { // If there is an error during the request
    console.error(error); // Log the error to the console
  } else { // If the request is successful
    // Parse the response body as JSON and get the results array
    const starWarsFilms = JSON.parse(body).results;

    // Initialize a counter for the number of times character ID 18 appears
    let numTimes = 0;

    // Loop through each film in the results
    for (const film of starWarsFilms) {
      // Loop through each character URL in the film's characters array
      for (const character of film.characters) {
        // Check if the character URL includes '18'
        if (character.includes('18')) {
          numTimes += 1; // Increment the counter if it does
        }
      }
    }

    // Log the number of times character ID 18 appears
    console.log(numTimes);
  }
});
