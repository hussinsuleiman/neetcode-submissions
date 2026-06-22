import sys

for line in sys.stdin:
    inputs = line.split()
    
    if inputs[1] == '^':
        x = pow(int(inputs[0]), int(inputs[2]), 10000)
    else:
        x = eval(line)
    
    print(x%10000)