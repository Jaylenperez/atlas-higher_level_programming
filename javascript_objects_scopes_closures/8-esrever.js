#!/usr/bin/node
// Export a function named 'esrever' that reverses a list
exports.esrever = function (list) {
  // Initialize an empty array to hold the reversed list
  const reversedList = [];

  // Loop through the original list starting from the last element to the first
  for (let i = list.length - 1; i >= 0; i--) {
    // Add the current element to the reversed list
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};
