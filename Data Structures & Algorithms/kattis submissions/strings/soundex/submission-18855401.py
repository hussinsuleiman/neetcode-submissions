import sys
code = [{'B', 'F', 'P', 'V'}, {'C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'}, {'D', 'T'}, {'L'}, {'M', 'N'}, {'R'}]

for line in sys.stdin:
    s = line.strip()
    cur = 0
    i = 0
    output = []
    
    while i < len(s):
        valid = False
        
        for j in range(6):
            if s[i] in code[j]:
                valid = True
                
                if cur != j+1:
                    cur = j+1
                    output.append(str(j+1))
                    
                break
        
        if not valid:
            cur = 0
            
        i += 1
    
    print(''.join(output))
    
    
    