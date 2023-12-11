vim -r 3-value_argument.js#!/usr/bin/node

if (process.argv.length === 0) {
	console.log('No argument');
} else {
	console.log(process.argv[2]);
}
