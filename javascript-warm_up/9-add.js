#!/usr/bin/node
// Define a function called 'add' that takes two arguments and returns their sum
function add (a, b) {
  return a + b;
}

// Get the command line arguments (excluding script name)
const numbersEntered = process.argv.slice(2);

// Parse the 1st and 2nd arguments as integers
const number = parseInt(numbersEntered[0], 10);
const number2 = parseInt(numbersEntered[1], 10);

// Calculate the sum using the 'add' function
const sum = add(number, number2);

// Print the result
console.log(sum);
