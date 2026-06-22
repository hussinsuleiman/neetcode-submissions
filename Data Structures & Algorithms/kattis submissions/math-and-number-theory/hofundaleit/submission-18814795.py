import sys
input = sys.stdin.readline

n, q = map(int, input().split())
books = []

for i in range(n):
    title, author = input().strip().split(', ')
    books.append((author, title))

books.sort()
dico = dict()

for i in range(n):
    dico[books[i][1]] = i+1 

for i in range(q):
    toRead = input().strip()
    
    if toRead in dico.keys():
        print(dico[toRead])
    else:
        print(-1)

    
        
    