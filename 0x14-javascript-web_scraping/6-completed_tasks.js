#!/usr/bin/node

const request = require('request');

// Check if the correct number of command line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <api-url>');
  process.exit(1); // Exit with an error code
}

const apiUrl = process.argv[2];

// Make an HTTP GET request to the specified API endpoint
request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(`Error making request: ${error.message}`);
    process.exit(1); // Exit with an error code
  }

  // Check if the request was successful (status code 200)
  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    process.exit(1); // Exit with an error code
  }

  // Count the number of completed tasks for each user
  const completedTasksCount = {};

  for (const task of body) {
    if (task.completed === true) {
      if (completedTasksCount[task.userId] === undefined) {
        completedTasksCount[task.userId] = 0;
      }
      completedTasksCount[task.userId]++;
    }
  }

  // Print the result
  console.log(completedTasksCount);
});
