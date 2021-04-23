#!/usr/bin/env python3

import sys
lines = sys.stdin
import string

def wordcount(filename):
    punc = string.punctuation
    d = {}
    for line in lines:
        words = line.lower().split()
        for l in words:
            l = l.strip(punc)
            if l not in d and l != " ":
                d[l] = 1
            elif l != " ":
                d[l] = d[l] + 1
    return d

d = wordcount(lines)

for k, v in sorted(d.items()):
    if len(k) > 3 and v >= 3 and k.isnumeric() == 0:
        maxv = len(str(max(d.values())))
        maxk = len((max(d.keys(), key=len)))
        print(f"{k:>{maxk - 3}} : {v:>{maxv}}")