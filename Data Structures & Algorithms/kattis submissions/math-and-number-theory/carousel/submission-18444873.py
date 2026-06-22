import sys
input = sys.stdin.readline

n, m = map(int, input().split())

while (n,m) != (0,0):
    ratioMin = float("inf")
    opt = (0, 0)
    
    for i in range(n):
        a, b = map(int, input().split())
        
        if a <= m and b / a <= ratioMin:
            if b / a < ratioMin or b > opt[1]:  
                opt = (a,b)
                
            ratioMin = b / a
    
    if opt == (0,0):
        print("No suitable tickets offered")
    else:
        print("Buy " + str(opt[0]) + " tickets for $" + str(opt[1]))
    
    n, m = map(int, input().split())
