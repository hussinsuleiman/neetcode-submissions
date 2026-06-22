from math import pi

w,h = map(int, input().split())
m = min(w,h)

if (m/2)**2*pi > w*h/2:
    print('circle')
elif 2*m >= max(w,h):
    print('square')
else:
    print('blank')