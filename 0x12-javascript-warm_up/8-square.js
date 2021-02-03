#!/usr/bin/node
// prints a square
const cast = parseInt(process.argv[2]);
let i = 0;
let j = 0;
let square = '';

if (!cast) {
  console.log('Missing size');
} else {
  for (i = 0; i < cast; i++) {
    for (j = 0; j < cast; j++) {
      square = square + 'X';
    }
    if (i < (cast - 1)) {
      square = square + '\n';
    }
  }
  console.log(square);
}
