N = int(input())
dSum = 0
k = N
nbDigits = 0

while k > 0:
    dSum += k%10
    k //= 10
    nbDigits += 1
    
small = [0] * nbDigits
large = [0] * nbDigits
indSmall = nbDigits-1
indLarge = 0

for i in range(dSum-1):
    if small[indSmall] == 9:
        indSmall -= 1
    small[indSmall] += 1

small[0] += 1

for i in range(dSum):
    if large[indLarge] == 9:
        indLarge += 1
    large[indLarge] += 1
    
small = [str(small[i]) for i in range(nbDigits)]
large = [str(large[i]) for i in range(nbDigits)]
print(''.join(small) + ' ' + ''.join(large))