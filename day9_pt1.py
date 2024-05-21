from aoc_utility import *

debug = False
test = False

input = ingestTextFile(("input/day9_input.txt", "input/day9_test_input.txt")[test])
output = 0

def same(list):
    return all(i == list[0] for i in list)

def extrapolate(order: int, curve: tuple):
    deltas = []
    for idx in range(len(curve[order]) - 1):
        deltas.append(
            curve[order][idx + 1] - curve[order][idx]
        )

    curve[order + 1] = deltas

    if not same(deltas):
        curve = extrapolate(order + 1, curve)
    else:
        curve[order + 1].append(deltas[0])

    curve[order].append(
        curve[order][-1] + curve[order + 1][-1]
    )
    return curve

for line in input:
    # Convert string input to integers
    points = []
    for number_string in line.split():
        points.append(int(number_string))
    
    # Seeding 1st order points
    curve = {1: points}

    curve = extrapolate(1, curve)

    output += curve[1][-1]

print("Day 9 - Part 1: " + str(output))