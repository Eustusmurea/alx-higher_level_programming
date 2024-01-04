#!/usr/bin/node

const fs = require('fs');

// Check if the command line argument for the file path is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1); // Exit with an error code
}

const filePath = process.argv[2];

// Read the file
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(`Error reading file: ${error.message}`);
  } else {
    console.log(data);
  }
});
