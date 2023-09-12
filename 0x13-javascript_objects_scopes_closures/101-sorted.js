#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDct = {};
for (let key in dict) {
  if (newDct[dict[key]] === undefined) {
    newDct[dict[key]] = [key];
  } else {
    newDct[dict[key]].push(key);
  }
}
console.log(newDct);
