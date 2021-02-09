#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs'); // import the fs module
const url = process.argv[2];
const file = process.argv[3];
request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  fs.writeFile(file, body, 'utf8', function (err) {
    if (err) return console.log(err);
  });
});
