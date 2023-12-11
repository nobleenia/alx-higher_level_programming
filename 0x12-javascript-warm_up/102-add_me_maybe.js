#!/usr/bin/node

exports.addMeMaybe = (x, func) => {
  const newNumber = x + 1;
  func(newNumber);
};
