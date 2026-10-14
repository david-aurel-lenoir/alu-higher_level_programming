#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const done = {};
    JSON.parse(body).forEach((t) => {
      if (t.completed) {
        done[t.userId] = (done[t.userId] || 0) + 1;
      }
    });
    console.log(done);
  }
});
