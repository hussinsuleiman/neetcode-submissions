import sys
input = sys.stdin.readline

N, C = map(int, input().split())

def count_perm_inversions_mod(N, C, MOD=10**9+7):
    dp = [0] * (C + 1)
    dp[0] = 1

    for n in range(2, N + 1):
        new = [0] * (C + 1)

        prefix = [0] * (C + 1)
        prefix[0] = dp[0]
        for k in range(1, C + 1):
            prefix[k] = (prefix[k - 1] + dp[k]) % MOD

        for k in range(C + 1):
            if k < n:
                new[k] = prefix[k] 
            else:
                new[k] = (prefix[k] - prefix[k - n]) % MOD

        dp = new

    return dp[C] % MOD

print(count_perm_inversions_mod(N, C))