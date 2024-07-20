#!/usr/bin/node

function printSquare (size) {
  // Convert the input to an integer
  const squareSize = parseInt(size);

  // Check if the conversion was successful
  if (isNaN(squareSize)) {
    console.log('Missing size');
    return;
  }

  // Print the square
  for (let i = 0; i < squareSize; i++) {
    let row = '';
    for (let j = 0; j < squareSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
}

// Get the first argument from the command line
const inputSize = process.argv[2];
printSquare(inputSize);
