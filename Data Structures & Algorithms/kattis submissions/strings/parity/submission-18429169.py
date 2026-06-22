import sys
input = sys.stdin.readline

line = input().strip()

while line != '#':
    nbOnes = 0
    
    for char in line:
        if char == '1':
            nbOnes += 1
    
    parity = line[-1]
    newLine = line[:-1]
    
    if parity == 'e':
        if nbOnes%2 == 0:
            print(newLine + '0')
        else:
            print(newLine + '1')
    
    elif nbOnes%2 == 0:
        print(newLine + '1')
    else:
        print(newLine + '0')
    
    line = input().strip()
        
    