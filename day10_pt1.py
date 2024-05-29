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

def shiftPos(exitDirection: str, pos: list):
    match exitDirection:
        case 'U':
            return [pos[0], pos[1] - 1]
        case 'D':
            return [pos[0], pos[1] + 1]
        case 'L':
            return [pos[0] - 1, pos[1]]
        case 'R':
            return [pos[0] + 1, pos[1]]

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
direction = getStartingDirection(pos, input)

steps = 0
while True:
    steps += 1
    pos = shiftPos(direction, pos)

    if input[pos[1]][pos[0]] == 'S':
        break

    direction = exitDirection(direction, input[pos[1]][pos[0]])

output = steps / 2

print("Day 10 - Part 1: " + str(output))