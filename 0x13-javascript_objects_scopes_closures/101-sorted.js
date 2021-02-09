#!/usr/bin/node
// Script that imports a dictionary of occurrences by user id and computes
// a dictionary of user ids by occurrence
const data = require('./101-data.js').dict;

let newDict = {};
newDict = Object.entries(data).reduce(function (hash, keys) {
  hash[keys[1]] = (hash[keys[1]] || []).concat(keys[0]);
  return hash;
}, {});

console.log(newDict);
