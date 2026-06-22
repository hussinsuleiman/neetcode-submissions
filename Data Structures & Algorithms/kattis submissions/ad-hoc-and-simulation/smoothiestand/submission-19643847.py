k,r = map(int, input().split())
ing = list(map(int, input().split()))
res = 0

for _ in range(r):
    amounts = list(map(int, input().split()))
    price = amounts.pop()
    m = 100000
    
    for i in range(k):
        if amounts[i] > 0:
            m = min(m, ing[i]//amounts[i])
    
    res = max(res, price*m)

print(res)