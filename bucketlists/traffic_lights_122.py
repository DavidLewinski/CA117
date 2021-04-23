#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def wait(length, red, green):  # inputs from line 37, recommended to follow comments from line 31 onwards.
    i = 0
    time = 0
#    print(length)
    red = int(red)  # turning from str to int
    green = int(green)  # turning from str to int
#    print('r', red)
#    print('g', green)
    while length >= time:  # loop until the time is greater than or eq to the length
        # for inputs of 1, 2, 1
        if i == 1:  # i != 1 therefore moves on
            time = time + green
            i = i - 1
        elif i == 0:  # as i == 0 it will update the time by adding the input for red
            time = time + red  # time = 2
            i = i + 1  # i is now == 1, as time is now == length the loop stops and moves on
    if i == 0:  # i is != 0, moves on
      wait = 0
    elif i == 1:  # i is == 1
      wait = time - length  # 2 - 1 = 1
#    print(wait)
    return (wait)  # wait is now 1

pdist = 0
length = 0
lenroad = lines[0]  # assigning first num to the length of the road, let this number be 5
for i in range(1, len(lines)):  # looping through all inputs in stdin after lines[0] as i = 1
    dist, red, green = lines[i].rstrip().split()  # assigning variables to those inputs from stdin
    dist = int(dist)  # turning from str to int
    pdist = int(pdist)  # turning from str to int
    length = length + (dist - pdist)  # updating the distance between lights, (1 = 0 + (1 - 0))
    length = length + wait(length, red, green)  # calling the function and running the new distance and lights through it, go to line 6.
    pdist = dist  # setting current distance as previous distance
time = (length + (int(lenroad) - pdist))
# (1(which is length from line 37, (1 = 0 + 1(line 27))) + 5(from str to int line[0] ie total road length) - 0(the previous distance, which is 0 as there is no previous))
print(time)  # the total of the previous step comes out to be 6 (for inputs of 5, 1, 2, 1)
