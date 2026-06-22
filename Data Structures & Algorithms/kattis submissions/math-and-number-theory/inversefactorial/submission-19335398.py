import math

s = input().strip()

small = {
    "1": 1,
    "2": 2,
    "6": 3,
    "24": 4,
    "120": 5,
    "720": 6
}

if s in small:
    print(small[s])
else:
    d = len(s)
    cur = 0.0
    i = 1

    while True:
        cur += math.log10(i)
        
        if int(cur) + 1 == d:
            print(i)
            break
        
        i += 1