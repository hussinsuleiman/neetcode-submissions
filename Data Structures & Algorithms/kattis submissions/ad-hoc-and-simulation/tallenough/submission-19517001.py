n = int(input())

for i in range(n):
    h = int(input())
    
    if h < 48:
        print("False")
        exit()

print("True")