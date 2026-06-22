import sys
input = sys.stdin.readline

def solve(board):
    if board[0][0] == '1':
        if board[1][1] == '-':
            return 0
        else:
            return 1
    
    if board[1][0] == '1':
        if board[1][1] == '-':
            return 4
        elif board[0][1] == '-':
            return 3
        else:
            return 2
    
    if board[0][1] == '1':
        if board[1][1] == '-':
            return 4
        elif board[1][0] == '-':
            return 3
        else:
            return 2
    
    if board[1][1] == '1':
        if board[0][0] == '-':
            return 6
        else:
            return 5
    
line1 = input()
line2 = input()
board = [line1, line2]

print(solve(board))