n = int(input())
tomato = 200/3

if n < 25:
    C = 2**(n-2)
    
    if n%2 == 0:
        tomato = 100*(2*C+1)/(3*C)
    else:
        tomato = 100*(2*C-1)/(3*C)

print(100-tomato, tomato)