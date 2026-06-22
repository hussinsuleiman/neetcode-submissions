R,G,B,k = map(int, input().split())
print(R+max(0,k-2) if (G==0 and B==0) else R+k)