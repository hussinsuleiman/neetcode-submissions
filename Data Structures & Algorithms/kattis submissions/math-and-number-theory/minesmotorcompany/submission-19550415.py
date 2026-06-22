N = int(input())
loc0 = input()
r0,c0 = loc0[0], loc0[1]
tot = 0

for _ in range(N-1):
    loc = input()
    r,c = loc[0], loc[1]
    tot += abs(ord(r)-ord(r0)) + abs(ord(c)-ord(c0))
    r0,c0 = r,c

print(tot)