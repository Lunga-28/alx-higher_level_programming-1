#!/usr/bin/node
// reads then prints the content of file

const filePath = process.argv[2];
const fs = require('fs');

fs.readFile(filePath, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
