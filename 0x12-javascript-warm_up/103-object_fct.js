#!/usr/bin/node

function createIncrementer() {
    let counter = 0;
  
    const incr = function (number) {
      counter += number;
    };
  
    const incrementAndCall = function (number, theFunction) {
      incr(number);
      theFunction(counter);
    };
  
    return incrementAndCall;
  }
  
  // Example usage:
  const myIncrementer = createIncrementer();
  
  myIncrementer(2, function(result) {
    console.log('Result:', result);
  });
  
  myIncrementer(3, function(result) {
    console.log('Result:', result);
  });
  