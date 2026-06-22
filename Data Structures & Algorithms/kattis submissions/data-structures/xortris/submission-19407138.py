m, n = map(int, input().split())
B = 0
board = []

for _ in range(m):
    line = input().strip()
    for ch in line:
        if ch == 'X':
            B ^= 1
    board.append(line)

if B == 1:
    print("impossible")
    exit()

if n == 1:
    board = [''.join(board)]

l = len(board)

if l == 1:
    arr = board[0]
    L = len(arr)
    flip = [0] * (L + 1)
    cur = 0

    for i in range(L):
        cur += flip[i]
        val = arr[i]

        if cur % 2 == 1:
            val = 'O' if val == 'X' else 'X'

        if val == 'X':
            if i + 4 > L:
                print("impossible")
                exit()
            cur += 1
            flip[i + 4] -= 1

    print("possible")

elif m == 2 and n == 2:
    cells = ''.join(board)
    if cells == '....' or cells == 'XXXX':
        print("possible")
    else:
        print("impossible")

else:
    print("possible")