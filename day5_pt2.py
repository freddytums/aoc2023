from aoc_utility import *
import os

test = False
debug = False

input = ingestTextFile(("input/day5_input.txt", "input/day5_test_input.txt")[test])
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
        self.destination_range_end = mapData[0] + (self.range - 1)
        self.source_range_start = mapData[1]
        self.source_range_end = mapData[1] + (self.range - 1)

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
    seedUsed = [False] * len(seeds)
    for mapData in mapSet:
        map = Map(mapData)
        for idx, seedData in enumerate(seeds):
            # print(idx)
            seed = Seed(seedData)
            
            if debug: 
                print("\n")
                print("Seed Data:")
                print("Start: ", str(seed.seed_range_start))
                print("End: ", str(seed.seed_range_end))
                print("Range: ", str(seed.range))
            
                print("\n")
                print("Source Data:")
                print("Source Start: ", str(map.source_range_start))
                print("Source End: ", str(map.source_range_end))
                print("Range: ", str(map.range))

                print("\n")
                print("Destination Data:")
                print("Dest Start: ", str(map.destination_range_start))
                print("Dest End: ", str(map.destination_range_end))
                print("Range: ", str(map.range))

                print("\n")
                print("Seed Used:")
                print(seedUsed[idx])
            if not seedUsed[idx]:
                if seed.seed_range_start < map.source_range_start:
                    if seed.seed_range_end >= map.source_range_start and seed.seed_range_end <= map.source_range_end:
                        if debug: print("---seed range below map range---")
                        # --|seed_range|-----
                        # ------|map_range|--
                        if debug: print([seed.seed_range_start, (map.source_range_start - 1) - seed.seed_range_start + 1])
                        if debug: print([map.destination_range_start, seed.seed_range_end - map.source_range_start + 1])
                        seeds.append([seed.seed_range_start, (map.source_range_start - 1) - seed.seed_range_start + 1])
                        seedUsed.append(False)
                        newSeeds.append([map.destination_range_start, seed.seed_range_end - map.source_range_start + 1])
                        seedUsed[idx] = True
                    elif seed.seed_range_end > map.source_range_end:
                        if debug: print("seed range eats map range")
                        if debug: print([seed.seed_range_start, (map.source_range_start - 1) - seed.seed_range_start + 1])
                        if debug: print([map.destination_range_start, map.range])
                        if debug: print([map.source_range_end + 1, (seed.seed_range_end - (map.source_range_end + 1) + 1)])
                        seeds.append([seed.seed_range_start, (map.source_range_start - 1) - seed.seed_range_start + 1])
                        seedUsed.append(False)
                        newSeeds.append([map.destination_range_start, map.range])
                        seedUsed[idx] = True
                        seeds.append([map.source_range_end + 1, (seed.seed_range_end - (map.source_range_end + 1) + 1)])
                        seedUsed.append(False)
                    else:
                        if debug: print("---whole lotta nothin!")
                        # nothing done, append and continue
                        # newSeeds.append([seed.seed_range_start, seed.range])
                elif seed.seed_range_start >= map.source_range_start:
                    if seed.seed_range_end <= map.source_range_end:
                        if debug: print("---seed range in map range---")
                        # ----|seed_range|------
                        # ----|map_range...|----
                        if debug: print([map.destination_range_start + (seed.seed_range_start - map.source_range_start), seed.range])
                        newSeeds.append([map.destination_range_start + (seed.seed_range_start - map.source_range_start), seed.range])
                        seedUsed[idx] = True
                    elif seed.seed_range_end > map.source_range_end and seed.seed_range_start <= map.source_range_end:
                        if debug: print("---seed range above map range---")
                        # --|seed_range...|--
                        # --|map_range|------
                        if debug: print([map.destination_range_start + (seed.seed_range_start - map.source_range_start), (map.source_range_end - seed.seed_range_start + 1)])
                        if debug: print([map.source_range_end + 1, (seed.seed_range_end - (map.source_range_end + 1) + 1)])
                        newSeeds.append([map.destination_range_start + (seed.seed_range_start - map.source_range_start), (map.source_range_end - seed.seed_range_start + 1)])
                        seedUsed[idx] = True
                        seeds.append([map.source_range_end + 1, (seed.seed_range_end - (map.source_range_end + 1) + 1)])
                        seedUsed.append(False)
                    else:
                        if debug: print("---whole lotta nothin!")
                        # nothing done, append and continue
                        # newSeeds.append([seed.seed_range_start, seed.range])
                else:
                    if debug: print("---whole lotta nothin!")
                    # nothing done, append and continue
                    # newSeeds.append([seed.seed_range_start, seed.range])

            # print(seeds)
            # print(newSeeds)
            # if debug: os.system("pause")

    # print(len(newSeeds))
    
    # print(seedUsed)
    # print(seeds)
    # print(newSeeds)

    i = 0
    for idx, seed in enumerate(seeds):
        i += seed[1]
        if not seedUsed[idx]:
            newSeeds.append(seed)
    
    i = 0
    for seed in newSeeds:
        i += seed[1]

    print("Total Seeds:")
    print(i)
    # print("Old Seeds:")
    # print(seeds)
    seeds = newSeeds.copy()
    # print("New Seeds:")
    # print(seeds)
    os.system("pause")

output = min(seeds)

print(output)

