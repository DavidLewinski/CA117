#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

nums = {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine", '10': "ten"}

def conv(line):
    a = []
    for i in line:
        if i in nums:
           a.append(nums[i])
        else:
            a.append("unknown")
    print(" ".join(a))

for line in lines:
    conv(line.rstrip().split())