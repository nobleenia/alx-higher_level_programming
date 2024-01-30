#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const [url, fileName] = process.argv.splice(2);
request(url.pipe(fs.createWriteStream(fileName));
