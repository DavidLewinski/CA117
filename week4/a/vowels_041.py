#!/usr/bin/env python3

import sys
lines = sys.stdin.read().lower()
vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for vowel in vowels:
    vlines = lines.count(str(vowel))
    vowels[vowel] = vlines

svowels = sorted(vowels.items(), key=lambda i: i[1], reverse=True)

maxlenv = 0
for i in svowels:
    v = i[1]
    if len(str(v)) > maxlenv:
        maxlenv = len(str(v))

for i in svowels:
    k = i[0]
    v = i[1]
    print(f"{k} : {v:>{maxlenv}}")