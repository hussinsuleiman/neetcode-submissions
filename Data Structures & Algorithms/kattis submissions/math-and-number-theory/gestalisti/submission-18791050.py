N = int(input())
guests = set()

for i in range(N):
    line = input().split()
    
    if line[0] == '+':
        guests.add(line[1])
    elif line[0] == '-':
        guests.remove(line[1])
    elif line[1] in guests:
        print("Jebb")
    else:
        print("Neibb")