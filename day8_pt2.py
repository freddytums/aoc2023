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
foundGoal = False
while not foundGoal:
    for step in steps:
        for idx, currentNode in enumerate(currentNodes):
            currentNodes[idx] = nodeDict[currentNode][step]
        output += 1

        allGoal = True
        for currentNode in currentNodes:
            if currentNode[2] != goal:
               allGoal = False

        # print(currentNodes)

        if allGoal:
            # print('All Found!')
            foundGoal = True
            break

print("Day 8 - Part 2: " + str(output))