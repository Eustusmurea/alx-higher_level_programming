#!/usr/bin/node

const request = require('request');

// Check if the correct number of command line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <film-number>');
  process.exit(1); // Exit with an error code
}

const filmNumber = process.argv[2];
const url = `http://swapi.co/api/films/${filmNumber}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error making request: ${error.message}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    return;
  }

  try {
    const data = JSON.parse(body);
    const name = data.title;
    console.log(name);
  } catch (parseError) {
    console.error(`Error parsing JSON: ${parseError.message}`);
    console.log('Raw Response Body:', body);
  }
});
