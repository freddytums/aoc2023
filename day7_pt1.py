from aoc_utility import *

from operator import *

debug = False
test = False

input = ingestTextFile(("input/day7_input.txt", "input/day7_test_input.txt")[test])
output = 0

cardRank = '23456789TJQKA'

def cardValue(card: str):
    try:
        return (cardRank.index(card) + 1)
    except:
        return 0

def type(hand: str):
    cardCounts = [0] * (len(cardRank) + 1)

    for card in hand:
        cardCounts[cardValue(card)] += 1

    if 5 in cardCounts:
        return 6
    elif 4 in cardCounts:
        return 5
    elif 3 in cardCounts:
        if 2 in cardCounts:
            return 4
        else:
            return 3
    elif countOf(cardCounts, 2) == 2:
        return 2
    elif 2 in cardCounts:
        return 1
    else:
        return 0

class Game():
    def __init__(self, gameData: str):
        self.hand = gameData.split()[0]
        self.bid = int(gameData.split()[1])
        self.type = type(self.hand)

gamesRankedList = []

for line in input:
    game = Game(line)

    if debug:
        print(game.hand)
        print(type(game.hand))
        print("\n")

    if len(gamesRankedList) == 0:
        gamesRankedList.append(
            [game.hand, game.bid, type(game.hand)]
        )

    for i, gameRanked in enumerate(gamesRankedList):
        if (game.type > gameRanked[2]) and (i == (len(gamesRankedList) - 1)):
            gamesRankedList.append(
                [game.hand, game.bid, type(game.hand)]
            )
            break
        elif game.type < gameRanked[2]:
            gamesRankedList.insert(
                i,
                [game.hand, game.bid, type(game.hand)]
            )
            break
        elif game.type == gameRanked[2]:
            for idx, card in enumerate(game.hand):
                finished = False
                cardA_value = cardValue(card)
                cardB_value = cardValue(gameRanked[0][idx])

                if cardA_value > cardB_value:
                    if i == (len(gamesRankedList) - 1):
                        gamesRankedList.append(
                            [game.hand, game.bid, type(game.hand)]
                        )
                        finished = True
                    break
                elif cardA_value < cardB_value:
                    gamesRankedList.insert(
                        i,
                        [game.hand, game.bid, type(game.hand)]
                    )
                    finished = True
                    break
            if finished:
                break

for idx, game in enumerate(gamesRankedList):
    output += (game[1] * (idx + 1))  

print("Day 7 - Part 1: " + str(output))