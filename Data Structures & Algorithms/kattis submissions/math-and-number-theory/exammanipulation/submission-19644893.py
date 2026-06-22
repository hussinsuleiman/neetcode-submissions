n,k = map(int, input().split())
students = [input() for _ in range(n)]
best = 0

for mask in range(1 << k):
    key = []

    for j in range(k):
        if (mask >> j) & 1:
            key.append('T')
        else:
            key.append('F')

    worst_score = k

    for student in students:
        score = 0

        for j in range(k):
            if student[j] == key[j]:
                score += 1

        worst_score = min(worst_score, score)

    best = max(best, worst_score)

print(best)