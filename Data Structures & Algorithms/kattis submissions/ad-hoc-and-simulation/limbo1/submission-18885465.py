T=int(input())
for i in range(T):
    L,R=map(int,input().split())
    print(1+(L+R)*(L+R+1)//2+R)