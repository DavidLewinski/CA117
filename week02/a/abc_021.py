#!/user/bin/env python3

import sys
lines = sys.stdin.readlines()

def ordered(numbers, abc):
    i = 0
    while i < len(numbers):
        j = i + 1
        while j < len(numbers):
            if int(numbers[j]) < int(numbers[i]):
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
            j = j + 1
        i = i + 1

    final = []
    A = numbers[0]
#    print(A)
    B = numbers[1]
#    print(B)
    C = numbers[2]
#    print(C)
    for current in abc:
        if current == "A":
            final.append(A)
        elif current == "B":
            final.append(B)
        elif current == "C":
            final.append(C)
    ans = " ".join(final)
#    print (ans)
    return ans

inpts = lines[0].split()
#print(inpts)
order = lines[1]
#print(order)
arranged = ordered(inpts, order)
print(arranged)
