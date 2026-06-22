M = int(input())
count = 0 
length = 1

while True:
    for half in range(1 << (length - 1), 1 << length):
        left = bin(half)[2:]
        right = left[-2::-1]  
        val = int(left + right, 2)
        count += 1
        
        if count == M:
            print(val)
            exit()

    for half in range(1 << (length - 1), 1 << length):
        left = bin(half)[2:]
        right = left[::-1]
        val = int(left + right, 2)
        count += 1
        
        if count == M:
            print(val)
            exit()

    length += 1