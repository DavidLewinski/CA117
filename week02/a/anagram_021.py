#!/usr/bin/env python3

import sys
def anagram(left, right):

  for c in left:
    if c in right:
      right = right.replace(c, "", 1)
    else:
      return False
  return right == ""

for line in sys.stdin:
  tokens = line.strip().split()
  left, right = tokens
  res = anagram(left, right)
  print(res)
