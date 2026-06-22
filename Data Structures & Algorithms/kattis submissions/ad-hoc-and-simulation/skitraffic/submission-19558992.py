hill = input()
time = input().split(':')
mins = int(time[0])*60 + int(time[1])
day = input()
weather = input()
snowed = input()
holiday = input()

if day in {'sat', 'sun'}:
    mins *= 2

if weather == '1':
    mins *= 2

if snowed == '1':
    mins *= 3

if holiday == '1':
    mins *= 3

h,m = mins//60, mins%60

if m < 10:
    m = '0' + str(m)

print(str(h) + ':' + str(m))