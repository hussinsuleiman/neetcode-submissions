N, s = input().split()
N = int(N)
output = []

def exp(a,b):
    if b == 0:
        return 1
    return a**(b%2) * (exp(a, b//2) ** 2) % 26

for i in range(N):
    output.append(chr((exp(2,i) + ord(s[i]) - ord('A')) % 26 + ord('A')))

print("".join(output))