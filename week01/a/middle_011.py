#!/usr/bin/env python3

import sys

for words in sys.stdin:
    words = words.strip()
    mid = len(words) // 2
    if len(words) % 2 == 1:
        print(words[mid])
    else:
        print("No middle character!")
