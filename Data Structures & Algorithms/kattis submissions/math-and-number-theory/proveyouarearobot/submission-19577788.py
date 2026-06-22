n,m = map(int, input().split())
board = []

def isPrime(k):
    if k == 1:
        return False
    
    for i in range(2, int(k**0.5)+1):
        if k%i == 0:
            return False
    return True

for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

ans = [['0']*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if isPrime(board[i][j]):
            ans[i][j] = '1'
    print(''.join(ans[i]))