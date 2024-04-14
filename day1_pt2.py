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
    first_num_idx = 999
    last_num_idx = -1
    for num_string in NumString.num_strings:
        if num_string in line:
            found_num_string_idx = line.find(num_string)
            found_num_int = NumString(num_string).num_int
            if (found_num_string_idx < first_num_idx):
                first_num_idx = found_num_string_idx
                first_num_int = found_num_int
            found_num_string_idx = line.rfind(num_string)
            found_num_int = NumString(num_string).num_int
            if (found_num_string_idx > last_num_idx):
                last_num_idx = found_num_string_idx
                last_num_int = found_num_int
    for idx, char in enumerate(line):
        if char.isnumeric():
            if idx < first_num_idx:
                first_num_idx = idx
                first_num_int = int(char)
            if idx > last_num_idx:
                last_num_idx = idx
                last_num_int = int(char)
    
    result = int(str(first_num_int) + str(last_num_int))
    output += result
            
print("Day 1 - Part 2: Sum of all calibration values: " + str(output))