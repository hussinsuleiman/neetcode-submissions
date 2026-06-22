board = []

for _ in range(4):
    row = input().split()
    
    for card in row:
        board.append(card)

ans = []

for i in range(12):
    for j in range(i+1, 12):
        for k in range(j+1, 12):
            c1, c2, c3 = board[i], board[j], board[k]
            valid = True
            
            for t in range(4):
                if not ((c1[t] == c2[t] and c2[t] == c3[t]) or (c1[t] != c2[t] and c1[t] != c3[t] and c2[t] != c3[t])):
                    valid = False    
                    break
            
            if valid:
                ans.append(str(i+1) + ' ' + str(j+1) + ' ' + str(k+1))

if not ans:
    print("no sets")
else:
    print('\n'.join(ans))