#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
length = 0

for line in lines:
    if len(line) > length:
        length = len(line)

for words in lines:
    centered = (f"{words.rstrip():^{length - 1}}")
    print(centered)
