N = int(input())
a = int(input())

if N == 1:
    print("Ja" if a % 2 == 0 else "Nej")
else:
    b = int(input())
    
    if N == 2:
        print("Nej" if (a % 2 == 0 and b % 2 == 0) else "Ja")
    else:
        c = int(input())
        
        print("Nej" if (a % 2 == 1 and b % 2 == 1 and c % 2 == 1) else "Ja")
    