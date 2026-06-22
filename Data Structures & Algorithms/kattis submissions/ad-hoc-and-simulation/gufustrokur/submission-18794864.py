n = int(input())
m = int(input())

print(min(abs(n-m), 360 - abs(n-m)))