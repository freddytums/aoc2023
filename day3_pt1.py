from aoc_utility import *

input = ingestTextFile("input/day3_input.txt")
output = 0



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

                    searchingLeft = True
                    while searchingLeft:
                        i = 1
                        if isInbounds(rowIdx - i, colIdx):
                            print(input[rowIdx - i][colIdx])
                            if input[rowIdx - i][colIdx].isnumeric():
                                validNumberMap[rowIdx - i][colIdx] = True
                            else:
                                searchingLeft = False
                        else:
                            searchingLeft = False
                        i += 1

                    searchingRight = True
                    while searchingRight:
                        i = 1
                        if isInbounds(rowIdx + i, colIdx):
                            print(input[rowIdx + i][colIdx])
                            if input[rowIdx + i][colIdx].isnumeric():
                                validNumberMap[rowIdx + i][colIdx] = True
                            else:
                                searchingRight = False
                        else:
                            searchingRight = False
                        i += 1

    return validNumberMap

validNumberMap = [[False] * len(input[0]) for i in range(len(input))]
specialCharacters = "@#$%&*"

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
                # print(int(''.join(number)))
                output += int(''.join(number))
                number = []

print("Day 3 - Part 1: " + str(output))