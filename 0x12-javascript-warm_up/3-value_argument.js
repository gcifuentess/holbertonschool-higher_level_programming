#!/usr/bin/node
// prints the first argument passed to it
const Argv2 = process.argv[2];
if (!Argv2) {
  console.log('No argument');
} else {
  console.log(Argv2);
}
