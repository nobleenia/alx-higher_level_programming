#!/usr/bin/node

const myVar1 = parseInt(process.argv[2]);
const myVar2 = parseInt(process.argv[3]);

function add (a, b) {
    if (isNaN(a) || isNaN(b)) {
	return NaN;
  }
  return a + b;
}

console.log(add(myVar1, myVar2));
