#!/usr/bin/node
// get the contents of a webpage and stores them in a file

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, 'utf8').pipe(fs.createWriteStream(file));
