#!/usr/bin/python3
def multiple_returns(sentence):
     len_s = len(sentence)
     if len_s == 0:
          tuple_s = (len_s, None)
     else:
          tuple_s = (len_s, sentence[0])
     return tuple_s
