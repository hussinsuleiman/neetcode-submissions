n,p = map(int, input().split())
pages = [int(input()) for i in range(n)]
rem = p

for i in range(n):
    if rem <= (i+1)*(pages[i]-1):
        print(i)
        exit()
    rem -= pages[i]
print(n)