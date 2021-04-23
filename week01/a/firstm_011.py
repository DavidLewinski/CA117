#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for words in lines:
  tokens = words.strip().split()
  i = 0
  while i < len(tokens):
    if tokens[i].startswith('m'):
      tokens[i] = tokens[i].capitalize()
      break
    i = i + 1
  print(' '.join(tokens))
