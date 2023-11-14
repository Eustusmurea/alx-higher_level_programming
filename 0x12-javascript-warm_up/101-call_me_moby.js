#!/usr/bin/node

function executeFunctionXTimes(n, func) {
    for (let i = 0; i < n; i++) {
      func();
    }
  }

function myFunction() {
    console.log('Executing myFunction');
  }

executeFunctionXTimes(3, myFunction);
