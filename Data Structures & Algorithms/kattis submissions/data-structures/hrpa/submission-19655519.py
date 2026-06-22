N = int(input())
fib = [1,1,2]

while fib[-1] < N:
    fib.append(fib[-1] + fib[-2])

i = -1

while fib[i] > N:
    N -= fib[i-1]
    i = 0
    
    while fib[i] < N:
        i += 1
    
print(N)