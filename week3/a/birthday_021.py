#!/usr/bin/env python3

import sys
import calendar
line = sys.stdin.readlines()

daysoftheweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
lines = ["Monday's child is fair of face", "Tuesday's child is full of grace", "Wednesday's child is full of woe", "Thursday's child has far to go", "Friday's child is loving and giving", "Saturday's child works hard for a living", "Sunday's child is fair and wise and good in every way"]

def day(date):
    day, month, year = date.split()
    return daysoftheweek[calendar.weekday(int(year), int(month), int(day))]

def sentences(date):
    day, month, year = date.split()
    return lines[calendar.weekday(int(year), int(month), int(day))]

for birthday in line:
    print(f"You were born on a {day(birthday)} and {sentences(birthday)}.")