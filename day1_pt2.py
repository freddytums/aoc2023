from aoc_utility import *

input = ingestTextFile("input/day1_input.txt")
output = 0

class NumString:
    num_int = 0

    num_strings = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]

    def __init__(self, string):
        for num_int, num_string in enumerate(self.num_strings):
            if string == num_string:
                self.num_int = num_int
    
for line in input:
    for num_string in NumString.num_strings:
        if num_string in line:
            num_string_idx = str.find(num_string)
            num_int = NumString(num_string).num_int
            
    

# print("Day 1 - Part 2: Sum of all calibration values: " + str(output))