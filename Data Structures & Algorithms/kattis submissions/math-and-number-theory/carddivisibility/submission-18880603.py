L,R = map(int,input().split())
print((R*(R+1)//2-(L-1)*L//2)%9)