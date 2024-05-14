from aoc_utility import *

import math

test = False

input = ingestTextFile(("input/day6_input.txt", "input/day6_test_input.txt")[test])
output = 1

class Races():
    def __init__(self, racesData):
        timesData = int(''.join(racesData[0].split()[1:]))
        distancesData = int(''.join(racesData[1].split()[1:]))

        self.race = []

        # for idx in range(len(timesData)):
        raceData = {
            'time': timesData, 
            'distance': distancesData
        }
        self.race.append(raceData)

def quadraticEquation(a, b, c):
    solution = []
    d = (b**2) - (4*a*c)  
    solution.append(
        (-b-math.sqrt(d))/(2*a)  
    )
    solution.append(
        (-b+math.sqrt(d))/(2*a)  
    )
    return solution

def winningTimes(raceData: list):
    return quadraticEquation(1, -raceData['time'], raceData['distance'])

def checkWin(holdTime: int, raceData):
    return ( (raceData['time'] - holdTime) * holdTime ) > raceData['distance']

a = Races(input)

for i in range(len(a.race)):
    print(a.race[i])
    [minTime, maxTime] = winningTimes(a.race[i])
    minTime = math.ceil(minTime)
    maxTime = math.ceil(maxTime) + 1
    count = maxTime - minTime

    if not checkWin(minTime, a.race[i]):
        count -= 1
    if not checkWin(maxTime, a.race[i]):
        count -= 1

    output *= count

print("Day 6 - Part 1: " + str(output))