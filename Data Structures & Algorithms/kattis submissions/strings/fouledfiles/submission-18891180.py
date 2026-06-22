n = int(input())

for i in range(n):
    s = input()
    output = []
    
    for j in range(0, len(s), 2):
        if len(output) == 40:
            break
        output.append(s[j])
    
    print("".join(output))