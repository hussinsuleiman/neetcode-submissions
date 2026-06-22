T = int(input())

for case in range(1, T+1):
    S = int(input())
    engines = [input() for i in range(S)]
    Q = int(input())
    cur = set(engines)
    res = 0
    
    for i in range(Q):
        query = input()
        
        if query in cur:
            cur.remove(query)
            
            if not cur:
                res += 1
                cur = set(engines)
                cur.remove(query)
    
    print('Case #' + str(case) + ': ' + str(res))