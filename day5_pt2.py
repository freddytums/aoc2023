from aoc_utility import *

debug = False

input = ingestTextFile(("input/day5_input.txt", "input/day5_test_input.txt")[debug])
output = 0

class Seed():
    def __init__(self, seedData: list):
        self.range = seedData[1]
        self.seed_range_start = seedData[0]
        self.seed_range_end = seedData[0] + seedData[1] - 1

class Map():
    def __init__(self, mapData: list):
        self.range = mapData[2]
        self.destination_range_start = mapData[0]
        self.destination_range_end = mapData[0] + range - 1
        self.source_range_start = mapData[1]
        self.source_range_end = mapData[1] + range - 1

seedsString = input[0].split(': ')[1].split(' ')
seeds = []
for i in range(int(len(seedsString) / 2)):
    seeds.append([int(seedsString[2*i]), int(seedsString[(2*i) + 1])])

almanacMaps = []
for line in input[2:]:
    if line[0].isalpha():
        mapSet = []
    elif len(line) == 1:
        almanacMaps.append(mapSet)
    else:
        destination_range_start = int(line.split(' ')[0])
        source_range_start = int(line.split(' ')[1])
        range = int(line.split(' ')[2])
        mapSet.append([destination_range_start, source_range_start, range])
almanacMaps.append(mapSet)

for mapSet in almanacMaps:
    newSeeds = []
    for mapData in mapSet:
        map = Map(mapData)
        for idx, seedData in enumerate(seeds):
            seed = Seed(seedData)

            if seed.seed_range_start < map.source_range_start:
                if seed.seed_range_end >= map.source_range_start and seed.seed_range_end <= map.source_range_end:
                    # --|seed_range|-----
                    # ------|map_range|--
                    pass
                pass
            elif seed.seed_range_start >= map.source_range_start:
                if seed.seed_range_end <= map.source_range_end:
                    # ----|seed_range|---
                    # ----|map_range|----
                    pass
                elif seed.seed_range_end > map.source_range_end:
                    # --|seed_range|-----
                    # ------|map_range|--
                    pass
                pass
            else:
                # nothing done, append and continue
                newSeeds.append([seed.seed_range_start, seed.range])
                pass

    seeds = newSeeds.copy()

output = min(seeds)

