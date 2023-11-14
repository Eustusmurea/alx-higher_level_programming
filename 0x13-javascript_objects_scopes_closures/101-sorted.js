#!/usr/bin/node

const occurrencesByUserId = require('./101-data');

function computeUserIdsByOccurrence(inputDict) {
  const resultDict = {};

  for (const userId in inputDict) {
    const occurrences = inputDict[userId];

    if (!resultDict[occurrences]) {
      resultDict[occurrences] = [];
    }

    resultDict[occurrences].push(userId);
  }

  return resultDict;
}

const userIdsByOccurrence = computeUserIdsByOccurrence(occurrencesByUserId);

console.log('User Ids by Occurrence:', userIdsByOccurrence);
