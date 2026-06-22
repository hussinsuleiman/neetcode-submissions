C,F = map(float, input().split())

for B in range(1, 10**6):
    A = max(1, int(B*(C-F)))
    
    if A < B*(C-F):
        A += 1
    
    if A <= B*(C+F):
        print(A)
        print(B)
        break