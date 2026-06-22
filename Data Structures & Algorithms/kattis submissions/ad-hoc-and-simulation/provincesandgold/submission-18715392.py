import sys
input = sys.stdin.readline

G, S, C = map(int, input().split())
power = 3*G + 2*S + C

bestTreasure = ""
bestVictory = ""

if power >= 8:
    bestVictory = "Province or "
elif power >= 5:
    bestVictory = "Duchy or "
elif power >= 2:
    bestVictory = "Estate or "

if power >= 6:
    bestTreasure = "Gold"
elif power >= 3:
    bestTreasure = "Silver"
else:
    bestTreasure = "Copper"

if bestVictory:
    print(bestVictory + bestTreasure)
else:
    print(bestTreasure)
