h0 = int(input())
h = h0

while (3*h*(h+1) // 2 - h) % 4 != 0:
    h += 1

print(h)