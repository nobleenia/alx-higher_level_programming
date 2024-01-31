#!/usr/bin/node

const writeFile = require('fs').writeFile;
const request = require('request');

const [url, fileName] = process.argv.splice(2);

request(url, (err, { body }) => {
  if (err) return console.log(err);
  writeFile(fileName, body, 'utf8', err => err && console.log(err));
});
