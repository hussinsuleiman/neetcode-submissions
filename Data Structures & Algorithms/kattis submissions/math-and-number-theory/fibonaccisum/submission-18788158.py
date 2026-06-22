import sys
input = sys.stdin.readline

n = int(input())
result = []
fib = [1, 1]

while fib[-1] <= n:
    fib.append(fib[-1] + fib[-2])

n -= fib[-2]
result.append(fib[-2])

while n > 0:
    i = 0
    
    while fib[i] <= n:
        i += 1
    
    n -= fib[i-1]
    result.append(fib[i-1])

output = []

for i in range(len(result)-1, -1, -1):
    output.append(str(result[i]))

print(" ".join(output))
    