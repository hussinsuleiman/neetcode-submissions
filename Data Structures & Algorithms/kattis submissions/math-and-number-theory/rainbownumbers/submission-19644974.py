MOD = 998244353

def minus_one(s):
    s = list(s)
    i = len(s) - 1

    while s[i] == '0':
        s[i] = '9'
        i -= 1

    s[i] = str(int(s[i]) - 1)

    s = ''.join(s).lstrip('0')
    return s if s else '0'


def count_up_to(s):
    if s == '0':
        return 0

    n = len(s)
    pow9 = [1] * (n + 1)
    
    for i in range(1, n + 1):
        pow9[i] = pow9[i - 1] * 9 % MOD

    ans = 0

    for length in range(1, n):
        ans += 9 * pow9[length - 1]
        ans %= MOD

    prev = -1

    for i in range(n):
        limit = int(s[i])
        remaining = n - i - 1

        for d in range(limit):
            if i == 0 and d == 0:
                continue
            if d == prev:
                continue

            ans += pow9[remaining]
            ans %= MOD

        if limit == prev:
            return ans
            
        prev = limit

    return (ans + 1) % MOD


L = input().strip()
U = input().strip()
answer = count_up_to(U) - count_up_to(minus_one(L))
print(answer % MOD)