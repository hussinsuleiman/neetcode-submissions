g,r = map(int, input().split())
res = 10*min(r,g)
g -= min(r,g)
res += g//3 * 10
g %= 3
if g == 1:
    res += 1
elif g == 2:
    res += 3
print(res)