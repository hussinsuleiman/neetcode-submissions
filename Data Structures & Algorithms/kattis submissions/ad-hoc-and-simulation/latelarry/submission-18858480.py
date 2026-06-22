line = input().split()
hours, minutes = map(int, line[0].split(":"))
t = int(input())

time = hours * 60 + minutes

if line[1] == 'PM' and hours != 12:
    time += 720
    
if hours == 12 and line[1] == 'AM':
    time -= 720

if time-t < 0:
    time += 1440

h, m = (time-t) // 60, (time-t) % 60

if m < 10:
    m = '0' + str(m)
else:
    m = str(m)

if h > 12:
    print(str(h-12) + ':' + m + ' PM')
    
elif h == 12:
    print('12:' + m + ' PM')

elif h == 0:
    print('12:' + m + ' AM')
    
else:
    print(str(h) + ':' + m + ' AM')
    
