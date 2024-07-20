#!/usr/bin/node

function factorial(n) {
    // Base case: Factorial of NaN is 1
    if (isNaN(n) || n < 0) {
        return 1;
    }

    // Recursive case: Compute factorial
    if (n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

// Get the first argument from the command line
const inputNumber = parseInt(process.argv[2], 10);

// Calculate the factorial
const result = factorial(inputNumber);

// Print the result
console.log(result);
