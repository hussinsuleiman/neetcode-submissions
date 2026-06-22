h,P = map(int, input().split())

for time in range(1, 8001):
    nbBulbs = (time+999)//1000
    K_inc = 60*time*P/100000
    K_lamp = 11*time*P/100000
    
    if 5*nbBulbs + K_inc > 60 + K_lamp:
        print((time+h-1)//h)
        exit()