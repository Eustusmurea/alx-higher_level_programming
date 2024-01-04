#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if the correct number of command line arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./script.js <url> <output-file-path>');
  process.exit(1); // Exit with an error code
}

const url = process.argv[2];
const path = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error making request: ${error.message}`);
    return;
  }

  // Check if the request was successful (status code 200)
  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    return;
  }

  // Write the response body to the specified file
  fs.writeFile(path, body, 'utf8', (writeError) => {
    if (writeError) {
      console.error(`Error writing to file: ${writeError.message}`);
    } else {
      console.log(`Response body written to ${path}`);
    }
  });
});

