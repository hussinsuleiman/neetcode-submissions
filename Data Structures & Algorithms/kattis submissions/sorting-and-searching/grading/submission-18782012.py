a,b,c,d,e = map(int, input().split())
grade = int(input())

if grade >= a:
    print("A")
elif grade >= b:
    print("B")
elif grade >= c:
    print("C")
elif grade >= d:
    print("D")
elif grade >= e:
    print("E")
else:
    print("F")
