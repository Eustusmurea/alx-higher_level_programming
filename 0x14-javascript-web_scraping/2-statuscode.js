#!/usr/bin/node

const request = require('request');

// Check if the correct number of command line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <url>');
  process.exit(1); // Exit with an error code
}

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(`Error making request: ${error.message}`);
    return;
  }

  console.log('Status Code:', response.statusCode);
});

