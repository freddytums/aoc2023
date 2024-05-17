from aoc_utility import *

import math

debug = False
test = False

input = ingestTextFile(("input/day8_input.txt", "input/day8_test_input.txt")[test])
output = 0

steps = input[0].strip()
nodeStrings = input[2:]

class Node():
    def __init__(self, nodeString: str):
        self.thisNode = nodeString.split()[0]
        self.leftNode = nodeString[7:10]
        self.rightNode = nodeString[12:15]

currentNodes = []
for nodeString in nodeStrings:
    node = Node(nodeString)
    if node.thisNode[2] == 'A':
        currentNodes.append(node.thisNode)

# print(currentNodes)

nodeDict = {}
for nodeString in nodeStrings:
    node = Node(nodeString)
    nodeDict[node.thisNode] = {'L':node.leftNode, 'R':node.rightNode}

goal = 'Z'
goalFrequency = [0] * len(currentNodes) 
for idx, currentNode in enumerate(currentNodes):
    foundGoal = False
    foundGoalAgain = False
    while not foundGoal or not foundGoalAgain:
        for step in steps:
            currentNodes[idx] = nodeDict[currentNodes[idx]][step]
            if foundGoal:
                goalFrequency[idx] += 1
                if currentNodes[idx][2] == goal:
                    foundGoalAgain = True
                    break

            if (currentNodes[idx][2] == goal) and not foundGoal:    
                foundGoal = True

output = math.lcm(*goalFrequency)

print("Day 8 - Part 2: " + str(output))