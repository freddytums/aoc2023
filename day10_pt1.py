from aoc_utility import *

debug = False
test = False

input = ingestTextFile(("input/day10_input.txt", "input/day10_test_input.txt")[test])
output = 0

# nav[direction entering from][pipe character] = 'direction exiting from'
nav = {
    'U': {
        '|': 'U',
        '7': 'L',
        'F': 'R',
    },
    'D': {
        '|': 'D',
        'J': 'L',
        'L': 'R',
    },
    'L': {
        '-': 'L',
        'L': 'U',
        'F': 'D',
    },
    'R': {
        '-': 'R',
        'J': 'U',
        '7': 'D',
    }
}
def exitDirection(enterDirection: str, pipeCharacter: str):
    return nav[enterDirection][pipeCharacter]

def findStart(input):
    for rowIdx, line in enumerate(input):
        for colIdx, char in enumerate(line):
            if char == 'S':
                return [colIdx, rowIdx]

def getStartingDirection(start, input):
    x = start[0]; y = start[1]

    if input[y - 1][x] in '|7F':
        return 'U'
    elif input[y + 1][x] in '|JL':
        return 'D'
    elif input[y][x + 1] in '-7J':
        return 'R'
    elif input[y][x - 1] in '-FL':
        return 'L'

pos = findStart(input)
start_direction = getStartingDirection(pos, input)

while input[pos[1]][pos[0]] != 'S':
    pass

print("Day 10 - Part 1: " + str(output))