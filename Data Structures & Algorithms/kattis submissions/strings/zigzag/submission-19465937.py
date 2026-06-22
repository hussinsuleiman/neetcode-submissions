k = int(input())

def max_possible(cur, r):
    if r == 0:
        return 0
    return max(cur, 25-cur) + 25*(r-1)

steps = (k+24)//25
res = [0]
cur = 0
remaining = k

for i in range(steps, 0, -1):
    for nxt in range(26):
        d = abs(nxt-cur)
        rem = remaining-d
        
        if 0 <= rem <= max_possible(nxt, i-1):
            res.append(nxt)
            cur = nxt
            remaining = rem
            break

print(''.join(chr(x + ord('a')) for x in res))