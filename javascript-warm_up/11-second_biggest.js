#!/usr/bin/node

function findSecondBiggest(args) {
    // Convert arguments to integers
    const integers = args.map(arg => parseInt(arg, 10));

    // Sort in descending order
    const sortedIntegers = integers.sort((a, b) => b - a);

    // Get the second biggest integer
    const secondBiggest = sortedIntegers[1] || 0;

    console.log(secondBiggest);
}

// Get the command line arguments (excluding the script name)
const inputArgs = process.argv.slice(2);
findSecondBiggest(inputArgs);
