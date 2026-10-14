#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    console.log(films.filter((f) => f.characters.some((c) => c.endsWith('/18/'))).length);
  }
});
