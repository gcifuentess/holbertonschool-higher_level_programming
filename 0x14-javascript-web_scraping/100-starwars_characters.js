#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const film = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + film + '/';
let data;
request(url, function (error, response, body) {
  if (error) console.error('error:', error); // Print the error if one occurred
  data = JSON.parse(body);
  data.characters.forEach(element => {
    request(element, function (error1, response1, body1) {
      if (error) console.error('error:', error1); // Print the error if one occurred
      console.log(JSON.parse(body1).name);
    });
  });
});
