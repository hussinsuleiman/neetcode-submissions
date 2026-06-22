a,b,c,d = map(int, input().split())
A,B,C,D = map(int, input().split())

if a+b+c+d > A+B+C+D:
    print("Gunnar")

elif a+b+c+d < A+B+C+D:
    print("Emma")

else:
    print("Tie")