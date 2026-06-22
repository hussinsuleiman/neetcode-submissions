import sys

for line in sys.stdin:
    line = line.strip()
    output = []
    curr = line[0]
    i = 1
    nb = 1
    
    while i < len(line):
        if line[i] == curr:
            nb += 1
        else:
            output.append(str(nb) + curr)
            nb = 1
            curr = line[i]
        
        i += 1
    
    output.append(str(nb) + curr)
    print("".join(output))
    
    
    
    