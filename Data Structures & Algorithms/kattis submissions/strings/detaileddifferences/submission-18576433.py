import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    orig = input().strip()
    new = input().strip()
    output = []
    l = len(new)
    
    for i in range(l):
        if orig[i] == new[i]:
            output.append(".")
        else:
            output.append("*")
    
    print(orig)
    print(new)
    print("".join(output))
    print()