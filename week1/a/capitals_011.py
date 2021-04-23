#!/usr/bin/env python3

import sys
a = sys.stdin.readlines()

for word in a:
    word = word.rstrip()
    caps1 = word[0].capitalize()
    middle = word[1:-1]
    caps2 = word[len(word) - 1].capitalize()
    if len(word) > 1:
        print(caps1 + middle + caps2)
