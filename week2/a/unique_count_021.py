#!/usr/bin/env python3

import sys
import string
lines = sys.stdin.readlines()
ordered = []

for line in lines:
    tokens = line.strip().split()
    for words in tokens:
        words = words.lower()
        for punc in words:
            if punc in string.punctuation:
                words = words.replace(punc, "", 1)

        if words not in ordered and len(words) > 0:
            ordered.append(words)

print(len(ordered))
