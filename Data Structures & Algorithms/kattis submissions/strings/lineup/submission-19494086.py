n = int(input())
s = [input() for i in range(n)]
new = s[:]
new.sort()

if new == s:
    print("INCREASING")
elif new[::-1] == s:
    print("DECREASING")
else:
    print("NEITHER")