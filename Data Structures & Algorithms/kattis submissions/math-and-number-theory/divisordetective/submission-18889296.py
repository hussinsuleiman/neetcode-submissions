N = int(input())
A, B = [N], [1]
i = 2
total = N

while i <= N:
    q = N // i
    A.append(q)
    B.append(N // q)
    i = N // q + 1

for i in range(len(A)-1):
    total += B[i] * (A[i] - A[i+1])

print(total)