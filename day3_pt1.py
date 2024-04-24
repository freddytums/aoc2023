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

def searchForAdjacentNums(SpecialChar_rowIdx, SpecialChar_colIdx, validNumberMap: list):
    for rowOffset in range(3):
        for colOffset in range(3):
            rowIdx = SpecialChar_rowIdx - 1 + rowOffset
            colIdx = SpecialChar_colIdx - 1 + colOffset
            
            if isInbounds(rowIdx, colIdx):
                if input[rowIdx][colIdx].isnumeric():
                    validNumberMap[rowIdx][colIdx] = True

    return validNumberMap

validNumberMap = [[False] * len(input[0]) for i in range(len(input))]

for rowIdx, line in enumerate(input):
    for colIdx, char in enumerate(line):
        if char in specialCharacters:
            validNumberMap = searchForAdjacentNums(rowIdx, colIdx, validNumberMap)

readingNumber = False
number = []  
for rowIdx, line in enumerate(input):
    for colIdx, char in enumerate(line):
        if validNumberMap[rowIdx][colIdx]:
            if not readingNumber:
                readingNumber = True
            number.append(char)
        else:
            if readingNumber:
                readingNumber = False
                print(number)
                output += int(number)
                number = []

            


print("Day 3 - Part 1: " + str(output))