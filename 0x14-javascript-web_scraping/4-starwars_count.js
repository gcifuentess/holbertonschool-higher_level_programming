#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = process.argv[2];
let data;
let characters = '';
const charID = '18'; // Wedge Antilles's  ID
let count = 0;
request(url, function (error, response, body) {
  if (error) console.error('error:', error); // Print the error if one occurred
  data = JSON.parse(body).results;
  for (let i = 0; i < data.length; i++) {
    characters = data[i].characters;
    characters.forEach(element => {
      element = '/' + element + '/';
      if (element.search(charID) > 0) {
        count += 1;
      }
    });
  }
  console.log(count);
});
