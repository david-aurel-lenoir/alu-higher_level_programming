#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number);

if (numbers.length < 2) {
  console.log(0);
} else {
  numbers.sort((a, b) => a - b);
  console.log(numbers[numbers.length - 2]);
}
