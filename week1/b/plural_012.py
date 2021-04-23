#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

vowels = ["a", "e", "i", "o", "u"]
end1 = ["x", "s", "z", "o"]
end2 = ["ch", "sh"]

for line in lines:
    line = line.strip()
    if line[len(line) - 1] in end1 or line[len(line) - 2:] in end2:
        print(line + "es")
    elif line[len(line) - 2] not in vowels and line[len(line) - 1] == "y":
        print(line[:len(line) - 1] + "ies")
    elif line[len(line) - 1] == "f":
        print(line[:len(line) - 1] + "ves")
    elif line[len(line) - 2:] == "fe":
        print(line[:len(line) - 2] + "ves")
    else:
        print(line + "s")
