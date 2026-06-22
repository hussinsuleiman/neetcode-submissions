s = input()
remaining = [4] * 10
unfilledT = set([i for i in range(10)])
unfilledF = set([i for i in range(10)])
boardT = [s[i] for i in range(10)]
boardF = [s[i] for i in range(10, 20)]
index = 20
card = s[index]
theta_turn = True

while True:
    while theta_turn:
        if not unfilledT:
            print("Theta wins")
            exit()
        
        if card == 'J':
            i = -1
            
            for t in range(10):
                if t in unfilledT and (i == -1 or remaining[t] < remaining[i]):
                    i = t
            
            unfilledT.remove(i)
            card = boardT[i]
        
        elif card == 'A':
            if 0 in unfilledT:
                unfilledT.remove(0)
                card = boardT[0]
                
            else:
                theta_turn = False
                index += 1
                card = s[index]
            
            remaining[0] -= 1
        
        elif card in {'2', '3', '4', '5', '6', '7', '8', '9'}:
            val = int(card) - 1
            
            if val in unfilledT:
                unfilledT.remove(val)
                card = boardT[val]
            
            else:
                theta_turn = False
                index += 1
                card = s[index]
            
            remaining[val] -= 1
        
        elif card == 'T':
            if 9 in unfilledT:
                unfilledT.remove(9)
                card = boardT[9]
                
            else:
                theta_turn = False
                index += 1
                card = s[index]
            
            remaining[9] -= 1
        
        else:
            theta_turn = False
            index += 1
            card = s[index]
            
        
    while not theta_turn:
        if not unfilledF:
            print("Theta loses")
            exit()
        
        if card == 'J':
            i = -1
            
            for t in range(10):
                if t in unfilledF:
                    i = t
                    break
            
            unfilledF.remove(i)
            card = boardF[i]
        
        elif card == 'A':
            if 0 in unfilledF:
                unfilledF.remove(0)
                card = boardF[0]
                
            else:
                theta_turn = True
                index += 1
                card = s[index]
            
            remaining[0] -= 1
        
        elif card in {'2', '3', '4', '5', '6', '7', '8', '9'}:
            val = int(card) - 1
            
            if val in unfilledF:
                unfilledF.remove(val)
                card = boardF[val]
            
            else:
                theta_turn = True
                index += 1
                card = s[index]
        
            remaining[val] -= 1
        
        elif card == 'T':
            if 9 in unfilledF:
                unfilledF.remove(9)
                card = boardF[9]
                
            else:
                theta_turn = True
                index += 1
                card = s[index]
        
            remaining[9] -= 1
        
        else:
            theta_turn = True
            index += 1
            card = s[index]