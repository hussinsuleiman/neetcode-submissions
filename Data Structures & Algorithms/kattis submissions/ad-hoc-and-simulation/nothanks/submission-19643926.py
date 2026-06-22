n = int(input())
cards = list(map(int, input().split()))
cards.sort()
score = cards[0]

for i in range(1, n):
    if cards[i] != cards[i-1]+1:
        score += cards[i]

print(score)