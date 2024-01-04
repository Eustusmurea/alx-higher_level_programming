#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error making request: ${error.message}`);
    return;
  }

  try {
    const result = JSON.parse(body).results;
    let count = 0;

    for (const movie of result) {
      for (const character of movie.characters) {
        if (character.includes('/18/') || character.includes('/18')) {
          count++;
        }
      }
    }

    console.log(count);
  } catch (parseError) {
    console.error(`Error parsing JSON: ${parseError.message}`);
    console.log('Raw Response Body:', body);
  }
});
