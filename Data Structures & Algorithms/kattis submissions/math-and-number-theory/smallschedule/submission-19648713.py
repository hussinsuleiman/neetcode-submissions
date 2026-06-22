Q,M,S,L = map(int, input().split())
x = M-L%M if L%M != 0 else 0 
print((L+M-1)//M*Q + (max(0, S - x*Q)+M-1)//M)