def catalan(n):
    c = [1]
    
    for k in range(n):
        c.append(c[-1] * (4*k + 2) // (k + 2))
        
    return c

q = int(input())
queries = []

for i in range(q):
    n = int(input())
    queries.append(n)

m = max(queries)
c = catalan(m)

for n in queries:
    print(c[n])