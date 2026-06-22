import sys

for line in sys.stdin:
    month, day, year, rises, sets = line.strip().split()
    hR, mR = map(int, rises.split(':'))
    hS, mS = map(int, sets.split(":"))
    
    hRes = hS - hR
    mRes = mS - mR
    
    if mR > mS:
        hRes -= 1
        mRes += 60
    
    print(month + ' ' + day + ' ' + year + ' ' + str(hRes) + ' hours ' + str(mRes) + ' minutes')