import sys
input = sys.stdin.readline

s0, s1, r0, r1 = map(int, input().split())

while (s0, s1, r0, r1) != (0, 0, 0, 0):
    if (s0, s1) == (1, 2) or (s0, s1) == (2, 1):
        if (r0, r1) == (1, 2) or (r0, r1) == (2, 1):
            print("Tie.")
        else:
            print("Player 1 wins.")
    
    elif (r0, r1) == (1, 2) or (r0, r1) == (2, 1):
        print("Player 2 wins.") 
    
    elif s0 == s1:
        if r0 == r1:
            if r0 > s0:
                print("Player 2 wins.") 
            elif r0 < s0:
                print("Player 1 wins.")
            else:
                print("Tie.")
        
        else:
            print("Player 1 wins.")
    
    elif r0 == r1:
        print("Player 2 wins.") 
    
    else:
        if s0 < s1:
            s0, s1 = s1, s0
        
        if r0 < r1:
            r0, r1 = r1, r0
        
        if s0 > r0:
            print("Player 1 wins.")
        
        elif s0 < r0:
            print("Player 2 wins.")
        
        elif s1 > r1:
            print("Player 1 wins.")
        
        elif s1 < r1:
            print("Player 2 wins.")
        
        else:
            print("Tie.")
    
    s0, s1, r0, r1 = map(int, input().split())