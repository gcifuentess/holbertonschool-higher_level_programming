#!/usr/bin/node
// reads and prints the content of a file
const file = process.argv[2];
const data = process.argv[3];
const fs = require('fs'); // import the fs module
fs.writeFile(file, data, 'utf8', function (err) {
  if (err) return console.log(err);
});
