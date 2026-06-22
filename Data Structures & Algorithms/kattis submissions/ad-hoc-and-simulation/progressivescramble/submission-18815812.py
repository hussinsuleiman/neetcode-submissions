import sys
input = sys.stdin.readline

def findVal(c):
    if c == ' ':
        return 0
    else:
        return ord(c) - ord('a') + 1
        
n = int(input())

for i in range(n):
    inp = input()
    command = inp[0]
    
    if command == 'e':
        values = [findVal(inp[2])]
        
        for j in range(3, len(inp)-1):
            values.append((values[-1] + findVal(inp[j])) % 27)
        
        output = []
        
        for v in values:
            if v == 0:
                output.append(' ')
            else:
                output.append(chr(v + ord('a') - 1))
        
        print(''.join(output))
    
    else:
        values = []
        
        for j in range(2, len(inp)-1):
            values.append(findVal(inp[j]))
        
        u = [values[0]]
        extra = 0
        
        for j in range(1, len(values)):
            if values[j-1] > values[j]:
                extra += 27
            
            u.append(values[j] + extra)
        
        orig = [u[0]]
        
        for j in range(1, len(u)):
            orig.append(u[j] - u[j-1])
        
        output = []
        
        for v in orig:
            if v == 0:
                output.append(' ')
            else:
                output.append(chr(v + ord('a') - 1))
        
        print(''.join(output))
            
            