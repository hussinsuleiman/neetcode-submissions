H,W,N,M = map(int, input().split())
image = [list(map(int, input().split())) for i in range(H)]
kernel = [list(map(int, input().split())) for i in range(N)]

result = [[0]*(W-M+1) for i in range(H-N+1)]

for i in range(H-N+1):
    for j in range(W-M+1):
        s = 0
        
        for x in range(N):
            for y in range(M):
                s += kernel[N-1-x][M-1-y] * image[i+x][j+y]
        
        result[i][j] = str(s)

for i in range(H-N+1):
    print(' '.join(result[i]))