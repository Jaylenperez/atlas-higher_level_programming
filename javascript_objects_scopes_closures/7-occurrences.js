#!/usr/bin/node
// Export a function named 'nbOccurences' that counts the occurrences of a specific element in a list
exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter to keep track of the total occurrences
  let totalOccurences = 0;

  // Loop through each element in the list
  for (let i = 0; i < list.length; i++) {
    // If the current element matches the search element, increment the counter
    if (list[i] === searchElement) {
      totalOccurences++;
    }
  }

  // Return the total number of occurrences found
  return totalOccurences;
};
