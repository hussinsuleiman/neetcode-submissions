n,m = map(int, input().split())
q,r = n//3, n%3

if r != 2:
    if m >= 2*q+2:
        print("Unnar")
    else:
        print("Arnar")
        
elif m > 2*q+2:
    print("Unnar")
else:
    print("Arnar")