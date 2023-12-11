#!/usr/bin/node

const myVar1 = process.argv[2];
const myVar2 = process.argv[3];

function add(a, b) {
  console.log(a + b);
}

add(myVar1, myVar2);
