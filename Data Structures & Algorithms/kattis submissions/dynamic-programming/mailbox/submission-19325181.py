import sys

INF = 10**30

def solve_case(K: int, M: int) -> int:
    dp = [[[0]*(M+1) for _ in range(M+1)] for __ in range(K+1)]

    for j in range(M+1):
        for k in range(j, M+1):
            dp[1][j][k] = (k*(k+1)//2) - (j*(j+1)//2)


    for i in range(2, K+1):
        for length in range(1, M+1):
            for j in range(0, M - length + 1):
                k = j + length
                best = INF

                for l in range(j+1, k+1):
                    cost = l + max(dp[i-1][j][l-1], dp[i][l][k])
                
                    if cost < best:
                        best = cost
                        
                dp[i][j][k] = best

    return dp[K][0][M]

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        k = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        out.append(str(solve_case(k, m)))
        
    print("\n".join(out))

if __name__ == "__main__":
    main()