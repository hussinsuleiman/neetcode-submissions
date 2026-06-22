a = int(input())
b = int(input())
c = int(input())
m = max(max(a,b),c)

if m > 90:
    print("Trubbig Triangel")
elif m == 90:
    print("Ratvinklig Triangel")
else:
    print("Spetsig Triangel")
