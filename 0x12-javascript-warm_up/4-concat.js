#!/usr/bin/node
if ((process.argv.length - 2) === 1) {
  console.log(process.argv[2] + ' is ' + 'undefined');
} else if ((process.argv.length - 2) > 1) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
  console.log('undefined' + ' is ' + 'undefined');
}
