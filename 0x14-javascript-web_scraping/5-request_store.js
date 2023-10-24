#!/usr/bin/node
// get the contents of a webpage and stores them in a file
let request = require('request');
let fs = require('fs');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  fs.writeFile(process.argv[3], body, function (err) {
    if (err) throw err;
  });
});
