#!/usr/bin/node
// prints the first argument passed to it
const Argv2 = process.argv[2];
if (!Argv2) {
  console.log('No argument');
} else {
  process.argv.forEach((val, index) => {
    if (index > 1) {
      console.log(val);
    }
  });
}
