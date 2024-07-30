#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Make a request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  // Parse the JSON response
  const todos = JSON.parse(body);
  const completedTasks = {};

  // Iterate through the todos and count completed tasks by user ID
  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId]++;
    }
  });

  // Print the result
  console.log(completedTasks);
});
