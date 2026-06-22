cnt = {}
voter = input()

while voter != '***':
    if voter in cnt:
        cnt[voter] += 1
    else:
        cnt[voter] = 1
    
    voter = input()

m = 0
res = 'Runoff!'

for v in cnt:
    if cnt[v] > m:
        m = cnt[v]
        res = v
    
    elif cnt[v] == m:
        res = 'Runoff!'

print(res)