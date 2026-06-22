P, H, T = map(int,input().split())
print(0 if P+H > T else 1 + (T-P-H)//(max(P,H)))
