a = int(input())
b = int(input())
m = int(input())
n = 1
subjects = [input() for i in range(m)]
verbs = [input() for i in range(m)]
objects = [input() for i in range(m)]
places = [input() for i in range(m)]

for i in range(m):
    phrase = []
    
    n = (a*n+b)%m
    phrase.append(subjects[n])
    
    n = (a*n+b)%m
    phrase.append(verbs[n])
    
    n = (a*n+b)%m
    phrase.append(objects[n])
    
    n = (a*n+b)%m
    phrase.append(places[n])
    
    print(' '.join(phrase) + '.')