import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    votes = []
    dico = {i: 0 for i in range(1, n+1)}
    
    for j in range(n):
        nbVotes = int(input())
        votes.append(nbVotes)
        dico[nbVotes] = j+1
    
    votes.sort()
    
    if votes[-1] == votes[-2]:
        print("no winner")
    elif sum(votes) >= 2*votes[-1]:
        print("minority winner " + str(dico[votes[-1]]))
    else:
        print("majority winner " + str(dico[votes[-1]]))