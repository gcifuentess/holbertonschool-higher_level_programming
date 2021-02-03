#!/usr/bin/node
// try to convert to int
const cast = parseInt(process.argv[2]);
if (!cast) {
  console.log('Not a number');
} else {
  console.log(`My number: ${cast}`);
}
