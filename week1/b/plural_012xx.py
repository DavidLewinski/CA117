#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    word = line.rstrip()
    if word.endswith("h"):
        word = (word + "es")
        print(word)
    elif word.endswith("fe"):
        word = (word[0:len(word) - 2] + "ves")
        print(word)
    elif word.endswith("ay"):
        word = (word + "s")
        print(word)
    elif word.endswith("x"):
        word = (word + "es")
        print(word)
    elif word.endswith("ss"):
        word = (word + "es")
        print(word)
    elif word.endswith("zz"):
        word = (word + "es")
        print(word)
    elif word.endswith("o"):
        word = (word + "es")
        print(word)
    elif word.endswith("ty"):
        word = (word[0:len(word) - 1] + "ies")
        print(word)
    elif word.endswith("f"):
        word = (word[0:len(word) - 1] + "ves")
        print(word)
    else:
        word = (word + "s")
        print(word)
