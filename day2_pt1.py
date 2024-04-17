from aoc_utility import *

input = ingestTextFile("input/day2_input.txt")
output = 0

max_red = 12; max_green = 13; max_blue = 14

def isItPossible(amount_of_cubes,color_of_cubes):
    match color_of_cubes:
        case "red":
            if amount_of_cubes > max_red:
                return False
        case "green":
            if amount_of_cubes > max_green:
                return False
        case "blue":
            if amount_of_cubes > max_blue:
                return False
    return True

for line in input:
    isPossible = True
    game_number = int(line.split(": ")[0].split(" ")[1])
    
    rounds = line.split(": ")[1].split("; ")
    for round in rounds:
        sets = round.split(", ")
        for set in sets:
            amount_of_cubes = int(set.split(" ")[0])
            color_of_cubes = set.split(" ")[1].strip()
            isPossible = isItPossible(amount_of_cubes, color_of_cubes)
            
            if not isPossible:
                break
        if not isPossible:
            break
    if not isPossible:
        continue
    
    if isPossible:
        output += game_number
            
print("Day 2 - Part 1: Sum of 'possible' Game's ID's: " + str(output))