n = int(input())
a = [str(i) for i in range(1, n+1)]
print("? " + ' '.join(a))

k = int(input())
print('! ' + str(k % (n*(n+1)//2)))