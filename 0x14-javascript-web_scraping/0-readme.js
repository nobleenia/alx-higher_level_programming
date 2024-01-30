#!/usr/bin/node
const fs = require('fs');
const fileName = process.arv[2];
fs.readFile(fileName, 'utf8', function (error, content) {
    console.log(error || content);
});
