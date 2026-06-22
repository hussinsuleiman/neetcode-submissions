n = int(input())

while n != 0:
    m = int((2*n-2)**(0.5))
    print(m if m*(m+1) >= 2*n-2 else m+1)
    n = int(input())