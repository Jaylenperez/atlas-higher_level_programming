#!/usr/bin/node

// Get the first argument from the command line
const numOccurrences = parseInt(process.argv[2]);

// Check if the argument is a valid positive integer
if (isNaN(numOccurrences)) {
  console.log('Missing number of occurrences');
} else if (numOccurrences > 0) {
  // Use a loop to print "C is fun" the specified number of times
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}
