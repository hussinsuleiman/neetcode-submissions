def kmp(pattern, text):
    m = len(pattern)
    lps = [0] * m
    j = 0
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    j = 0
    
    for x in text:
        while j > 0 and x != pattern[j]:
            j = lps[j - 1]
        if x == pattern[j]:
            j += 1
            if j == m:
                return True
    return False

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
MOD = 360000

a.sort()
b.sort()

d1 = [(a[(i + 1) % n] - a[i]) % MOD for i in range(n)]
d2 = [(b[(i + 1) % n] - b[i]) % MOD for i in range(n)]

if kmp(d2, d1 + d1):
    print("possible")
else:
    print("impossible")
