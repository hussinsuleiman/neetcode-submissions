import math

N = int(input())
a = int(math.log(N)/math.log(2))+1
print(a)
res = [str(2**i) for i in range(a)]
print(" ".join(res))

