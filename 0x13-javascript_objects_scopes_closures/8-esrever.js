#!/usr/bin/node
// returns the reversed version of a list
exports.esrever = function (list) {
  if (!list || list.length < 2) {
    return list;
  }
  let temp = 0;
  const len = list.length;
  for (let i = 0; i < (len / 2); i++) {
    temp = list[i];
    list[i] = list[len - i - 1];
    list[len - i - 1] = temp;
  }
  return list;
};
