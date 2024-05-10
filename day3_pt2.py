from aoc_utility import *

input = ingestTextFile("input/day3_input.txt")
output = 0

def isInbounds(rowIdx, colIdx):
    if rowIdx < 0 or rowIdx > 139:
        return False
    if colIdx < 0 or colIdx > 139:
        return False  
    return True

def numberGrab(searchRow, searchCol):
    number = []
    columnOffset = 1
    lookingForFirstDigit = True
    while lookingForFirstDigit:
        if isInbounds(searchRow, searchCol - columnOffset):
            if input[searchRow][searchCol - columnOffset].isnumeric():
                columnOffset += 1
            else:
                lookingForFirstDigit = False
        else:
            lookingForFirstDigit = False
    grabbingNumber = True
    while grabbingNumber:
        if isInbounds(searchRow, searchCol - columnOffset + 1):
            if input[searchRow][searchCol - columnOffset + 1].isnumeric():
                number.append(input[searchRow][searchCol - columnOffset + 1])

                temp_input = list(input[searchRow])
                temp_input[searchCol - columnOffset + 1] = '.'
                input[searchRow] = temp_input

                columnOffset -= 1
            else:
                grabbingNumber = False
        else:
            grabbingNumber = False

    return int(''.join(number))
        
def search(rowIdx, colIdx):
    global output
    numbersFound = 0
    numbers = [0, 0]
    for rowOffset in range(3):
        for colOffset in range(3):
            searchRow = rowIdx + rowOffset - 1; searchCol = colIdx + colOffset - 1
            if isInbounds(searchRow, searchCol):
                if input[searchRow][searchCol].isnumeric():
                    numbers[numbersFound] = numberGrab(searchRow, searchCol)
                    numbersFound += 1

    if numbersFound == 2:
        output += numbers[0] * numbers[1]


for rowIdx, line in enumerate(input):
    for colIdx, char in enumerate(line):
        if char == '*':
            search(rowIdx, colIdx)

print("Day 3 - Part 2: " + str(output))