from aoc_utility import *

debug = False

input = ingestTextFile(("input/day5_input.txt", "input/day5_test_input.txt")[debug])
output = 0

seeds = input[0].split(': ')[1].split(' ')
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

almanacMaps = []
for line in input[2:]:
    if line[0].isalpha():
        map = []
    elif len(line) == 1:
        almanacMaps.append(map)
    else:
        destination_range_start = int(line.split(' ')[0])
        source_range_start = int(line.split(' ')[1])
        range = int(line.split(' ')[2])
        map.append([destination_range_start, source_range_start, range])
almanacMaps.append(map)

for mapSet in almanacMaps:
    newSeeds = seeds.copy()
    for map in mapSet:
        for idx, seed in enumerate(seeds):
            if (seed >= map[1]) and (seed < (map[1] + map[2])):
                newSeeds[idx] = (map[0] + (seed - map[1]))

    seeds = newSeeds.copy()

output = min(seeds)

print("Day 5 - Part 1: " + str(output))