#!/usr/bin/env python3

import sys
lines = sys.stdin
d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

for line in lines:
    line = line.split()
    converted = []
    for numbers in line:
        try:
            number = int(numbers)
            if number <= 19 and number >= 0:
                converted.append(d[number])
            elif number <= 99:
                if number % 10 != 0:
                    converted.append(tens[int(numbers[0]) - 2] + "-" + d[int(numbers[-1:])])
                else:
                    converted.append(tens[int(numbers[0]) - 2])
            elif number == 100:
                converted.append('one hundred')
        except ValueError:
            converted.append("unknown")

    print(" ".join(converted))