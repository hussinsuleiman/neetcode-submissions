pa,ka,pb,kb,n = map(int, input().split())
INF = float('inf')
i,j,cost = 0,0,INF
index = 0

while (n - index*ka) >= 0:
    if index * pa + ((n - index*ka + kb-1)//kb) * pb < cost:
        i = index
        j = (n - index*ka + kb-1)//kb
        cost = i * pa + j * pb
        
    index += 1

print(str(i) + ' ' + str(j) + ' ' + str(cost))