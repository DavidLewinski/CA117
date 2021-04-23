#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

seventeen = []
eighteenplus = []
four_letters = []
twoq = []
cie = []
anagrams = []

def checka(line):
    return len([c for c in line if "a" in c.lower()])
def checkq(line):
    return len([c for c in line if "q" in c.lower()])
def anagram(left, right):

  for c in left:
    if c in right:
      right = right.replace(c, "", 1)
    else:
      return False
  return right == ""

for line in lines:
    line = line.rstrip()
    loweredline = line.rstrip().lower()
    if len(line) == 17:
        seventeen.append(line)
    if len(line) >= 18:
        eighteenplus.append(line)
    if checka(loweredline) == 4:
        four_letters.append(line)
    if checkq(loweredline) >= 2:
        twoq.append(line)
    if "cie" in loweredline:
        cie.append(line)
    angleana = anagram(loweredline, "angle")
    if angleana and loweredline != "angle":
        anagrams.append(line)

print("Words containing 17 letters:", seventeen)
print("Words containing 18+ letters:", eighteenplus)
print("Words with 4 a's:", four_letters)
print("Words with 2+ q's:", twoq)
print("Words containing cie:", cie)
print("Anagrams of angle:", anagrams)