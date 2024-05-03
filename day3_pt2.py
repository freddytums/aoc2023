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
    countOfAdjactentNums = 0
    numbers = [[],[]]
    for rowOffset in range(3):
        for colOffset in range(3):
            rowIdx = SpecialChar_rowIdx - 1 + rowOffset
            colIdx = SpecialChar_colIdx - 1 + colOffset
            
            if isInbounds(rowIdx, colIdx) and not validNumberMap[rowIdx][colIdx]:
                print("Row: " + str(rowIdx) + " Col: " + str(colIdx))
                countOfAdjactentNums += 1
                if input[rowIdx][colIdx].isnumeric():
                    numbers[countOfAdjactentNums].append(input[rowIdx][colIdx])
                    validNumberMap[rowIdx][colIdx] = True

                    searchingLeft = True
                    i = 1
                    while searchingLeft:
                        if isInbounds(rowIdx, colIdx - i):
                            if input[rowIdx][colIdx - i].isnumeric():
                                validNumberMap[rowIdx][colIdx - i] = True
                                numbers[countOfAdjactentNums].insert(0, input[rowIdx][colIdx])
                            else:
                                searchingLeft = False
                        else:
                            searchingLeft = False
                        i += 1

                    searchingRight = True
        
                    i = 1
                    while searchingRight:
                        if isInbounds(rowIdx, colIdx + i):
                            if input[rowIdx][colIdx + i].isnumeric():
                                validNumberMap[rowIdx][colIdx + i] = True
                                numbers[countOfAdjactentNums].append(input[rowIdx][colIdx])
                            else:
                                searchingRight = False
                        else:
                            searchingRight = False
                        i += 1
    print(numbers)
    return validNumberMap

validNumberMap = [[False] * len(input[0]) for i in range(len(input))]
specialCharacters = "*"

for rowIdx, line in enumerate(input):
    for colIdx, char in enumerate(line):
        if char in specialCharacters:
            validNumberMap = searchForAdjacentNums(rowIdx, colIdx, validNumberMap)

print("Day 3 - Part 2: " + str(output))