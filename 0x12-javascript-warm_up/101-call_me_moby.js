#!/usr/bin/node

exports.callMeMoby = (x, func) => {
  for (let i = 0; i < x; i++) {
    func();
  }
};
