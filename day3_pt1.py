from aoc_utility import *

input = ingestTextFile("input/day3_input.txt")
output = 0

specialCharacters = "@#$%&*"

def isInbounds(rowIdx, colIdx):
    if rowIdx < 0 or rowIdx > 139:
        return False
    if colIdx < 0 or colIdx > 139:
        return False  
    return True

def searchForNums(SpecialChar_rowIdx, SpecialChar_colIdx):
    for rowOffset in range(3):
        for colOffset in range(3):
            rowIdx = SpecialChar_rowIdx - 1 + rowOffset
            colIdx = SpecialChar_colIdx - 1 + colOffset
            
            if isInbounds(rowIdx, colIdx):
                if input[rowIdx][colIdx].isnumeric():
                    lookingForFirstDigit = True

    return

for rowIdx, line in enumerate(input):
    for colIdx, char in enumerate(line):
        if char in specialCharacters:
            searchForNums(rowIdx, colIdx)
        

print("Day 3 - Part 1: " + str(output))