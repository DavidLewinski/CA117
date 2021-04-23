#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
vowel_set = "aeiou"

def sss(line):
    totale = 0
    totaliary = 0
    shortvowel = ""
    moste = []
    for line in lines:
        line = line.strip()
        lline = line.strip().lower()
        haseveryvowel = False
        if "a" in lline and "e" in lline and "i" in lline and "o" in lline and "u" in lline:
            haseveryvowel = True

        if haseveryvowel:
            if shortvowel == "":
                shortvowel = line
            elif len(shortvowel) > len(lline):
                shortvowel = line
        lengthoflline = len(lline)
        if lengthoflline > 4 and line[lengthoflline - 4:] == "iary":
            totaliary = totaliary + 1

        if lline.count("e") > totale:
            moste = []
            moste.append(line)
            totale = lline.count("e")
        elif lline.count("e") == totale:
            moste.append(line)
            totale = lline.count("e")

    print(f'Shortest word containing all vowels: {str(shortvowel)}')
    print(f'Words ending in iary: {str(totaliary)}')
    print(f"Words with most e's: {str(moste)}")

sss(lines)