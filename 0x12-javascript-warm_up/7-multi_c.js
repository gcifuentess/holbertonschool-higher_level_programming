#!/usr/bin/node
// prints x times “C is fun”
const cast = parseInt(process.argv[2]);
let i = 0;
if (!cast) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < cast; i++) {
    console.log('C is fun');
  }
}
