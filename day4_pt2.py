from aoc_utility import *

input = ingestTextFile("input/day4_input.txt")
output = 0

class lotteryCard():
    def __init__(self, cardString: str):
        self.winningNumbersString = cardString.split(':')[1].split('|')[0]
        self.drawnNumbersString = cardString.split(':')[1].split('|')[1]
        self.winningNumbers = [
            int(self.winningNumbersString[1:3]),
            int(self.winningNumbersString[4:6]),
            int(self.winningNumbersString[7:9]),
            int(self.winningNumbersString[10:12]),
            int(self.winningNumbersString[13:15]),
            int(self.winningNumbersString[16:18]),
            int(self.winningNumbersString[19:21]),
            int(self.winningNumbersString[22:24]),
            int(self.winningNumbersString[25:27]),
            int(self.winningNumbersString[28:30]),
        ]
        self.drawnNumbers = [
            int(self.drawnNumbersString[1:3]),
            int(self.drawnNumbersString[4:6]),
            int(self.drawnNumbersString[7:9]),
            int(self.drawnNumbersString[10:12]),
            int(self.drawnNumbersString[13:15]),
            int(self.drawnNumbersString[16:18]),
            int(self.drawnNumbersString[19:21]),
            int(self.drawnNumbersString[22:24]),
            int(self.drawnNumbersString[25:27]),
            int(self.drawnNumbersString[28:30]),
            int(self.drawnNumbersString[31:33]),
            int(self.drawnNumbersString[34:36]),
            int(self.drawnNumbersString[37:39]),
            int(self.drawnNumbersString[40:42]),
            int(self.drawnNumbersString[43:45]),
            int(self.drawnNumbersString[46:48]),
            int(self.drawnNumbersString[49:51]),
            int(self.drawnNumbersString[52:54]),
            int(self.drawnNumbersString[55:57]),
            int(self.drawnNumbersString[58:60]),
            int(self.drawnNumbersString[61:63]),
            int(self.drawnNumbersString[64:66]),
            int(self.drawnNumbersString[67:69]),
            int(self.drawnNumbersString[70:72]),
            int(self.drawnNumbersString[73:75]),
        ]

copies = [1] * len(input)

for cardNumber, line in enumerate(input):
    card = lotteryCard(line)

    score = 0
    for winningNumber in card.winningNumbers:
        if winningNumber in card.drawnNumbers:
            score += 1
    
    for i in range(score):
        copies[cardNumber + i + 1] += (copies[cardNumber])

for i in copies:
    output += i

print("Day 4 - Part 2: " + str(output))