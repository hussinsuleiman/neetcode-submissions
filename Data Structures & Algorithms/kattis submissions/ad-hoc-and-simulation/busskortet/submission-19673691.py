K = int(input())

if K%100 != 0:
    K += 100-K%100

res = K//500
K %= 500

if K > 0:
    res += K//200
    K %= 200
    
    if K > 0:
        res += K//100
        K %= 100
        
        if K > 0:
            res += 1

print(res)