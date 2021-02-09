#!/usr/bin/node
// reads and prints the content of a file
const file = process.argv[2];
const fs = require('fs'); // import the fs module
fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
