#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (e) => {
      if (e) {
        console.log(e);
      }
    });
  }
});
