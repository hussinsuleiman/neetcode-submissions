start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))
h,m,s = 0,0,0

if start[0] < 12 and end[0] >= 12:
    h = 1

m = end[0] - start[0]

if m < 0:
    m += 60

s = end[1] - start[1] + 60*m
print(str(h) + ' ' + str(m) + ' ' + str(s))