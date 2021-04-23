#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
input_text = sys.argv[1]

with open(input_text, "r") as f:
    inputs = f.readlines()

for line in lines:
    line = line.strip().split()
    i = 0
    while i < len(line):
        word = line[i]
        for censortext in inputs:
            censortext = censortext.strip()
            if censortext in word:
                line[i] = word.replace(censortext, "@" * len(censortext))
        i = i + 1
    print(" ".join(line))