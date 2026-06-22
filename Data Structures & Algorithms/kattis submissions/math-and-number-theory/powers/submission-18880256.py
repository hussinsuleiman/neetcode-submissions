a,b = map(int, input().split())
print(0 if a%2==1 else ((a//2)**b)%a)