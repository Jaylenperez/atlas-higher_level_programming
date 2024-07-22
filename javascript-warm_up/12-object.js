#!/usr/bin/node
const myObject = {
    type: 'object',
    value: 12
  };
  console.log(myObject); // This will log { type: 'object', value: 12 }

  // Update the value property of myObject
  myObject.value = 89;

  console.log(myObject); // This will now log { type: 'object', value: 89 }
