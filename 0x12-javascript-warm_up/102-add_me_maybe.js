#!/usr/bin/node

function createIncrementer() {
    let counter = 0;
  
    const incrementAndCall = function (number, theFunction) {
      counter += number;
      theFunction(counter);
    };
  
    return incrementAndCall;
  }
  
  // Example usage:
  const myIncrementer = createIncrementer();
  
  myIncrementer(2, function(result) {
    console.log('Result:', result); // Output: Result: 2
  });
  
  myIncrementer(3, function(result) {
    console.log('Result:', result); // Output: Result: 5
  });
  