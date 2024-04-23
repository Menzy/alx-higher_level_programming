#!/usr/bin/node
// import { process.argv } from 'node:process';

if (process.argv[2] == null) {
  console.log('No argument');
} else if (process.argv[2] !== null) {
  console.log(process.argv[2]);
}
