N = int(input())
b = bin(N)[2:]
rev = b[::-1]
print(int(rev,2))