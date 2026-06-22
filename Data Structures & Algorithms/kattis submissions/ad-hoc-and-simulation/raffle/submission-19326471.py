import math

def log_comb(n, k):
    return math.lgamma(n+1) - math.lgamma(k+1) - math.lgamma(n-k+1)

def prob(n, m, p):
    lp = math.log(m) + log_comb(n, p-1) - log_comb(n+m, p)
    return math.exp(lp)

def solve(n, p):
    t = (n + 1 - p) // (p - 1)
    t = max(1, t)
    candidates = [t, t+1]
    best_m = None
    best_prob = -1

    for m in candidates:
        pr = prob(n, m, p)
        if pr > best_prob:
            best_prob = pr
            best_m = m

    return best_prob

n,p = map(int, input().split())
print(solve(n,p))