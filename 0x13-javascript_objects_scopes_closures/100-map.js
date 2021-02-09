#!/usr/bin/node
// imports an array and computes a new array

const list = require('./100-data.js').list;
console.log(list);
const map1 = list.map((x, idx) => x * idx);
console.log(map1);
