import sys
input = sys.stdin.readline

n = int(input())

while n != 0:
    output = ['?'] * 32
    
    for i in range(n):
        command = input().strip().split()    
        c = command[0]
        k = 31-int(command[1])
        
        if c == 'SET':
            output[k] = '1'
        
        elif c == 'CLEAR':
            output[k] = '0'
        
        else:
            m = 31-int(command[2])
            
            if c == 'OR':
                if output[k] == '1' or output[m] == '1':
                    output[k] = '1'
                elif output[k] == '?' or output[m] == '?':
                    output[k] = '?'
                else:
                    output[k] = '0'
            
            elif c == 'AND':
                if output[k] == '1' and output[m] == '1':
                    output[k] = '1'
                elif output[k] == '0' or output[m] == '0':
                    output[k] = '0'
                else:
                    output[k] = '?'
    
    print("".join(output))
    n = int(input())