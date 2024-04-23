#!/usr/bin/node
function calcFactorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * calcFactorial(n - 1);
  }
}

const num = parseInt(process.argv[2]);
if (!isNaN(num)) {
  console.log(calcFactorial(num));
} else {
  console.log('1');
}
