n = int(input())

if n < 2:
    print(n)
    exit()

fib = [1,1]
res = 2

while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
    res += 1
    
print(res)