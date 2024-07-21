from aoc_utility import *

debug = False
test = False

input = ingestTextFile(("input/day12_input.txt", "input/day12_test_input.txt")[test])
output = 0

class Map:
    def __init__(self, map_string: str):
        self.map_string         = map_string
        self.map_length         = len(map_string)
        self.countOfMissing     = self.map_string.count('?')
        self.indicesOfMissing   = [i for i in range(self.map_length) if self.map_string[i] == '?']
        self.countOfOperational = self.map_string.count('.')
        self.countOfDamaged     = self.map_string.count('#')
        self.maxCountOfMaps     = 2 ** self.countOfMissing

        self.getArrangementsFromMap()

    def getArrangementsFromMap(self):
        countOfDamaged = 0
        self.arrangements = []
        for spring in self.map_string:
            if spring == '#':
                countOfDamaged += 1
            elif countOfDamaged != 0:
                self.arrangements.append(countOfDamaged)
                countOfDamaged = 0
        if countOfDamaged != 0:
            self.arrangements.append(countOfDamaged)

class Record():
    def __init__(self, line: str):
        # String, map of missing, operational, and damaged springs
        self.map_string         = line.split()[0]
        self.Map                = Map(self.map_string)

        # List of integer values, listing the size of contiguous groups that should exists in the map
        self.arrangements       = list(map(int,(line.split()[1]).split(','))) 
        self.numberOfGroups     = len(self.arrangements)
        self.goalCountOfDamaged = sum(self.arrangements)

        self.createListOfTestMaps()

        self.countHowManyPossibleArrangements()

    def createListOfTestMaps(self):
        self.TestMaps = []
        for i in range(self.Map.maxCountOfMaps):
            potentialPattern = list(map(int, bin(i)[2:].zfill(self.Map.countOfMissing)))
            if (sum(potentialPattern) + self.Map.countOfDamaged) == self.goalCountOfDamaged:
                temp_map = list(self.map_string)
                for idx, damaged in enumerate(potentialPattern):
                    if damaged:
                        temp_map[self.Map.indicesOfMissing[idx]] = '#'
                    else:
                        temp_map[self.Map.indicesOfMissing[idx]] = '.'
                temp_map = "".join(temp_map)
                self.TestMaps.append(Map(temp_map))
         
    def isTestMapASolution(self, TestMap: Map):
        if TestMap.countOfMissing != 0:
            return False
        if TestMap.countOfDamaged != self.goalCountOfDamaged:
            return False
        if TestMap.map_length != self.Map.map_length:
            return False
        if TestMap.arrangements == self.arrangements:
            return True    

    def countHowManyPossibleArrangements(self):
        self.countOfSolutions = 0
        for TestMap in self.TestMaps:
            if self.isTestMapASolution(TestMap):
                self.countOfSolutions += 1

for line in input:
    Data = Record(line)

    output += Data.countOfSolutions

print("Day 12 - Part 1: " + str(output))