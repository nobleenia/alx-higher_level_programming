#!/usr/bin/node

exports.esrever = function (list) {
  let first = 0;
  let last = list.length - 1;
  while (first < last) {
    const temp = list[first];
    list[first] = list[last];
    list[last] = temp;
    first++;
    last--;
  }
  return list;
};
