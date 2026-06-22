import sys
input = sys.stdin.readline

n = int(input())
notes = []

for i in range(n):
    note = input().strip()
    
    for j in range(len(note)):
        notes.append(note[j])

notes.reverse()
print("".join(notes))