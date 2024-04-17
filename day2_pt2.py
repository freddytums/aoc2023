from aoc_utility import *

input = ingestTextFile("input/day2_input.txt")
output = 0

def updateMinimums(minimums, amount_of_cubes, color_of_cubes):
    match color_of_cubes:
        case "red":
            if amount_of_cubes > minimums[0]:
                minimums[0] = amount_of_cubes
        case "green":
            if amount_of_cubes > minimums[1]:
                minimums[1] = amount_of_cubes
        case "blue":
            if amount_of_cubes > minimums[2]:
                minimums[2] = amount_of_cubes 
    return minimums

for line in input:
    game_number = int(line.split(": ")[0].split(" ")[1])
    
    minimums = [0, 0, 0] #Red, Green, Blue

    rounds = line.split(": ")[1].split("; ")
    for round in rounds:
        sets = round.split(", ")
        for set in sets:
            amount_of_cubes = int(set.split(" ")[0])
            color_of_cubes = set.split(" ")[1].strip()
            minimums = updateMinimums(minimums, amount_of_cubes, color_of_cubes)

    power = minimums[0] * minimums[1] * minimums[2]
    output += power

print("Day 2 - Part 2: Sum of power of sets " + str(output))