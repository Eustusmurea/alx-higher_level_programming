#!/usr/bin/node

const fs = require('fs');
const path = require('path');

function concatFiles(file1Path, file2Path, destinationPath) {
  const content1 = fs.readFileSync(file1Path, 'utf8');
  const content2 = fs.readFileSync(file2Path, 'utf8');
  const concatenatedContent = content1 + content2;

  fs.writeFileSync(destinationPath, concatenatedContent, 'utf8');
  console.log('Files concatenated successfully!');
}

if (process.argv.length !== 5) {
  console.error('Usage: node concatFiles.js file1Path file2Path destinationPath');
  process.exit(1);
}

const file1Path = path.resolve(process.argv[2]);
const file2Path = path.resolve(process.argv[3]);
const destinationPath = path.resolve(process.argv[4]);

concatFiles(file1Path, file2Path, destinationPath);
