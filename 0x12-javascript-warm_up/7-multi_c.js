#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (isNan(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
