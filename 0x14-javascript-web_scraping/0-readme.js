#!/usr/bin/node
// reads then prints the content of file
let fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) { console.log(err); } else { process.stdout.write(data); }
});
