N = int(input())
i = 2
done = False

while i*i <= N:
    if N%i == 0:
        print(N-N//i)
        done = True
        break
    
    i += 1

if not done:
    print(N-1)