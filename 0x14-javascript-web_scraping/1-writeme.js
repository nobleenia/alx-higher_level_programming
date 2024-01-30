#!/usr/bin/node
const fs = require('fs');
const [fileName, content] = process.argv.slice(2);
fs.writeFile(fileName, content, error => {
    if (error) console.log(error);
});
