n = int(input())
perm = list(map(int, input().split()))
p = int(input())

for _ in range(p):
    rank = list(map(int, input().split()))
    tot = 0
    
    for i in range(n):
        for j in range(n):
            if rank[j] == perm[i]:
                tot += j-i
                
                for k in range(j-1, i-1, -1):
                    rank[k+1], rank[k] = rank[k], rank[k+1]
                
                break
            
    print(tot)