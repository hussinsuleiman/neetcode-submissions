i = int(input())
l, w, h = 0, 0, 3

if i == 1:
    l = int(input())
    w = l

elif i == 2:
    w = int(input())
    l = int(input())

else:
    w = int(input())
    l = int(input())
    h = int(input())

print(2*h*(l+w) - 4*h + (l-2)*(w-2))