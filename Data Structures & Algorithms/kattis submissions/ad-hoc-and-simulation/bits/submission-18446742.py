import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    inp = input().strip()
    nb = 0
    maxOnes = 0
    
    for k in range(len(inp)):
        nb = nb * 10 + int(inp[k])
        binary = str(bin(nb))
        nbOnes = 0
        
        for bit in binary:
            if bit == '1':
                nbOnes += 1
    
        if nbOnes > maxOnes:
            maxOnes = nbOnes
    
    print(maxOnes)
    