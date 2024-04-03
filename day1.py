from aoc_utility import *

input = ingestTextFile("input/day1_input.txt")
output = 0

for line in input:
    for char in line:
        if char.isnumeric():
            first_digit = char
            break
    for char in line[::-1]:
        if char.isnumeric():
            second_digit = char
            break
    result = int(first_digit + second_digit)
    output += result

print("Day 1 - Part 1: Sum of all calibration values: " + str(output))