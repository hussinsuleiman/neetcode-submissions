def solve(a, bit, ans):
    if bit < 0:
        for x in a:
            ans[x] = x
        return
    
    zero, one = [], []
    mask = 1 << bit
    
    for x in a:
        if x & mask:
            one.append(x)
        else:
            zero.append(x)
    
    if one:
        solve(one, bit-1, ans)
    
    if zero:
        solve(zero, bit-1, ans)
    
    for x in one:
        y = x ^ mask
        ans[x], ans[y] = ans[y], ans[x]

n = int(input())
a = [int(input()) for i in range(n)]
ans = {}
solve(a, 59, ans)

for x in a:
    print(ans[x])