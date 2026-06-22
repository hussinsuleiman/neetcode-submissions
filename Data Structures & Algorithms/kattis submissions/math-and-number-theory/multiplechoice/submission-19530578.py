N = int(input())
answers = [input() for i in range(N)]
M = int(input())
d = {}
IDs = []
grades = [[] for i in range(N+1)]

for _ in range(M):
    S = int(input())
    IDs.append(S)
    guesses = [input() for i in range(N)]
    res = 0
    
    for i in range(N):
        if guesses[i] == answers[i]:
            res += 1
    
    d[S] = res
    grades[res].append(S)

IDs.sort()
order = input()

for i in range(N+1):
    grades[i].sort()

if order == "STUDENT_ID_ASC":
    for S in IDs:
        print(str(S) + ' ' + str(d[S]))

elif order == "STUDENT_ID_DESC":
    IDs = IDs[::-1]
    
    for S in IDs:
        print(str(S) + ' ' + str(d[S]))

elif order == "GRADE_ASC":
    for i in range(N+1):
        g = grades[i]
        
        for elt in g:
            print(str(elt) + ' ' + str(i))
    
elif order == "GRADE_DESC":
    for i in range(N, -1, -1):
        g = grades[i]
        
        for elt in g:
            print(str(elt) + ' ' + str(i))