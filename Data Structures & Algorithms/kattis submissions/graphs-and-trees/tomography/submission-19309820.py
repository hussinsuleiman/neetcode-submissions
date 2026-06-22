def feasible(rows, cols):
    rows = sorted(rows, reverse=True)

    if sum(rows) != sum(cols):
        return 'No'

    for k in range(1, len(rows)+1):
        left = sum(rows[:k])
        right = sum(min(c, k) for c in cols)
        if left > right:
            return 'No'

    return 'Yes'

m,n = map(int, input().split())
rows = list(map(int, input().split()))
cols = list(map(int, input().split()))
print(feasible(rows, cols))