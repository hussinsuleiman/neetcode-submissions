import sys
input = sys.stdin.readline

L = int(input())
H, G = 0, 0

for i in range(L):
    M, N, K = map(int, input().split())
    board = []
    Hwins, Gwins = False, False
    
    for k in range(N):
        board.append(input().strip())
            
    for k in range(N):
        nbXcons = 0
        nbOcons = 0
        
        for l in range(M):
            if board[k][l] == 'x':
                nbXcons += 1
                nbOcons = 0
            elif board[k][l] == 'o':
                nbOcons += 1
                nbXcons = 0
            else:
                nbOcons = 0
                nbXcons = 0
            
            if nbXcons == K:
                H += 1
                Hwins = True
                break
            if nbOcons == K:
                G += 1
                Gwins = True
                break
        
        if Hwins or Gwins:
            break
    
    if (not Hwins) and (not Gwins):
        for k in range(M):
            nbXcons = 0
            nbOcons = 0
            
            for l in range(N):
                if board[l][k] == 'x':
                    nbXcons += 1
                    nbOcons = 0
                elif board[l][k] == 'o':
                    nbOcons += 1
                    nbXcons = 0
                else:
                    nbOcons = 0
                    nbXcons = 0
                
                if nbXcons == K:
                    H += 1
                    Hwins = True
                    break
                if nbOcons == K:
                    G += 1
                    Gwins = True
                    break
            
            if Hwins or Gwins:
                break
    
    if (not Hwins) and (not Gwins):
        for k in range(N-K+1):
            for l in range(M-K+1):
                nbXcons = 0
                nbOcons = 0
                
                for m in range(K):
                    if board[k+m][l+m] == 'x':
                        nbXcons += 1
                        nbOcons = 0
                    elif board[k+m][l+m] == 'o':
                        nbOcons += 1
                        nbXcons = 0
                    else:
                        nbOcons = 0
                        nbXcons = 0
                    
                    if nbXcons == K:
                        H += 1
                        Hwins = True
                        break
                    if nbOcons == K:
                        G += 1
                        Gwins = True
                        break
            
                if Hwins or Gwins:
                    break
            
            if Hwins or Gwins:
                break
    
    if (not Hwins) and (not Gwins):
        for k in range(N-K+1):
            for l in range(K-1, M):
                nbXcons = 0
                nbOcons = 0
                
                for m in range(K):
                    if board[k+m][l-m] == 'x':
                        nbXcons += 1
                        nbOcons = 0
                    elif board[k+m][l-m] == 'o':
                        nbOcons += 1
                        nbXcons = 0
                    else:
                        nbOcons = 0
                        nbXcons = 0
                    
                    if nbXcons == K:
                        H += 1
                        Hwins = True
                        break
                    if nbOcons == K:
                        G += 1
                        Gwins = True
                        break
            
                if Hwins or Gwins:
                    break
            
            if Hwins or Gwins:
                break

print(str(H) + ":" + str(G))