#!/usr/bin/env python3

def factorial(num):
    if num == 0:
        return 1
    return (num * factorial(num - 1))
