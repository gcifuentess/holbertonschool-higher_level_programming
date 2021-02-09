#!/usr/bin/node
// Computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];
let data;
const newDict = {};
request(url, function (error, response, body) {
  if (error) console.error('error:', error); // Print the error if one occurred
  data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed === true) {
      if (newDict[data[i].userId]) newDict[data[i].userId] += 1;
      else newDict[data[i].userId] = 1;
    }
  }
  console.log(newDict);
});
