P = int(input())

def mult(A,B,MOD):
    row1 = [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD]
    row2 = [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    return [row1, row2]
    
def power(M, exp, MOD):
    cur = [[1,0],[0,1]]
    
    if exp%2 == 1:
        cur = M
        
    if exp//2 == 0:
        return cur
    
    prev = power(M, exp//2, MOD)
    temp = mult(prev, prev, MOD)
    return mult(temp, cur, MOD)

for i in range(P):
    K,Y = map(int, input().split())
    M = [[1,1],[1,0]]
    MOD = 10**9
    P = power(M, Y-1, MOD)
    print(str(K) + ' ' + str(sum(P[1])%MOD))