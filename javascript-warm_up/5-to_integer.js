#!/usr/bin/node
const input = process.argv[2]; // Retrieve the first command-line argument and store it in the 'input' variable.

const parsedInt = parseInt(input); // Attempt to convert the input to an integer and store the result in 'parsedInt'

if (!isNaN(parsedInt)) { // Check if 'parsedInt' is a valid integer (not NaN)
  console.log(`My number: ${parsedInt}`); // If valid, print the converted integer
} else {
  console.log('Not a number'); // Otherwise, print "Not a number"
}
