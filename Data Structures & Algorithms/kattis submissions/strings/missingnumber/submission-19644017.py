n = int(input())
s = input()
index = 0

for i in range(1, n+1):
    l = len(str(i))
    
    if str(i) != s[index:index+l]:
        print(i)
        exit()
    
    index += l