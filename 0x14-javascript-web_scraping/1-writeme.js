#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of command line arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file-path> <content>');
  process.exit(1); // Exit with an error code
}

const filePath = process.argv[2];
const content = process.argv[3];

// Write to the file
fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.error(`Error writing to file: ${error.message}`);
  } else {
    console.log(`Content written to ${filePath}`);
  }
});

