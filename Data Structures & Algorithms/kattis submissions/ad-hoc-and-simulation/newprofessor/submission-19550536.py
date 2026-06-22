C = int(input())

if C < 5:
    print(C)
    exit()

S = [int(input()) for i in range(C)]
S.sort()
res = 0

while True:
    for k in range(-1, -6, -1):
        if S[k] == 0:
            print(res)
            exit()
        
        S[k] -= 1
        res += 1
    
    S.sort()