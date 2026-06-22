import sys
input = sys.stdin.readline

n, m = map(int, input().split())
teams = [i for i in range(1, n+1)]

for _ in range(m):
    teamA, teamB = input().split()
    indexA = int(teamA[1:])
    indexB = int(teamB[1:])

    rankA = teams.index(indexA)
    rankB = teams.index(indexB)

    if rankA > rankB:
        teams.remove(indexB)
        rankA = teams.index(indexA)
        teams.insert(rankA + 1, indexB)

print(' '.join(f"T{t}" for t in teams))

