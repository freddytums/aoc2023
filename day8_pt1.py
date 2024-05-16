from aoc_utility import *

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
        
nodeDict = {}
for nodeString in nodeStrings:
    node = Node(nodeString)
    nodeDict[node.thisNode] = {'L':node.leftNode, 'R':node.rightNode}

currentNode = 'AAA'
goal = 'ZZZ'
foundGoal = False
while not foundGoal:
    for step in steps:
        currentNode = nodeDict[currentNode][step]
        output += 1
        if currentNode == goal:
            foundGoal = True
            break

print("Day 8 - Part 1: " + str(output))