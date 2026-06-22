import sys

input = sys.stdin.readline

def weighted_median(weights):
    total = sum(weights)
    half = (total + 1) // 2
    cur = 0
    
    for i, w in enumerate(weights):
        cur += w
        
        if cur >= half:
            return i

def cost(weights, center):
    total = 0
    
    for i, w in enumerate(weights):
        total += w * abs(i - center)
        
    return total

T = int(input())

for _ in range(T):
    C, R = map(int, input().split())
    row_weight = [0] * R
    col_weight = [0] * C

    for i in range(R):
        row = list(map(int, input().split()))
        row_weight[i] = sum(row)

        for j in range(C):
            col_weight[j] += row[j]

    best_row = weighted_median(row_weight)
    best_col = weighted_median(col_weight)
    ans = cost(row_weight, best_row) + cost(col_weight, best_col)
    print(ans, "blocks")