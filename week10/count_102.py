#!/usr/bin/env python3

def count_letters(num):
    if num == '':
        return 0
    else:
        return (count_letters(num[1:]) + 1)
