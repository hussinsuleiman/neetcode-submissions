import sys
case = 1

for line in sys.stdin:
    print("Case " + str(case) + ':')
    n = int(line)
    nbs = [int(sys.stdin.readline()) for i in range(n)]
    sums = set()
    
    for i in range(n):
        for j in range(i+1, n):
            sums.add(nbs[i] + nbs[j])
    
    sums = list(sums)
    sums.sort()
    l = len(sums)
    
    m = int(sys.stdin.readline())
    
    for _ in range(m):
        x = int(sys.stdin.readline())
        i,j = 0,l-1
        done = False
        
        while i <= j:
            mid = (i+j)//2
            
            if sums[mid] == x:
                print("Closest sum to " + str(x) + " is " + str(x) + ".")
                done = True
                break
            
            elif sums[mid] < x:
                i = mid+1
            
            else:
                j = mid-1
        
        if done:
            continue
        
        if j == -1:
            print("Closest sum to " + str(x) + " is " + str(sums[0]) + ".")
        
        elif i == l:
            print("Closest sum to " + str(x) + " is " + str(sums[l-1]) + ".")
        
        elif x - sums[j] <= sums[i] - x:
            print("Closest sum to " + str(x) + " is " + str(sums[j]) + ".")
        
        else:
            print("Closest sum to " + str(x) + " is " + str(sums[i]) + ".")
        
    case += 1