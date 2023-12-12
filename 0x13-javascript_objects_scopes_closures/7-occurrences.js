#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const count = 0;
  for (const i in list) {
    if (list[i] === searchElement){
      count++;
    }
  }
  return count;
};
