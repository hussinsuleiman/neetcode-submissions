import sys
input = sys.stdin.readline

P = int(input())

def factorial(k):
    if k == 1:
        return 1
    else:
        return k * factorial(k-1)

for i in range(P):
    K, S = map(int, input().split())
    nbTwo = S // 2
    total = 0
    
    if S > 3:
        if nbTwo%2 == 1:
            nbTwo -= 1
        
        nbOnes = S - 2 * nbTwo
        
        if nbOnes == 0:
            total += 1
        else:
            total += (nbTwo // 2 + 1) ** 2
            
        nbOnes += 4
        nbTwo -= 2
        
        while nbOnes <= nbTwo:
            temp = 1
            
            for k in range(nbOnes // 2, 0, -1):
                temp *= (nbTwo // 2 + k)  
            
            total += (temp // factorial(nbOnes // 2)) ** 2
            nbOnes += 4
            nbTwo -= 2

    print(str(K) + " " + str(total))    