#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode
//  number matches a given integer.
const request = require('request');
const film = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + film + '/';
request(url, function (error, response, body) {
  if (error) console.error('error:', error); // Print the error if one occurred
  console.log(JSON.parse(body).title); // Print the response status code if a response was received
});
