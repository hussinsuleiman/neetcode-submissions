import sys
input = sys.stdin.readline

n = int(input())
case = 1

while n != 0:
    occ = dict()
    
    for i in range(n):
        name = input().strip().split()
        animal = name[-1].lower()
        
        if animal in occ.keys():
            occ[animal] += 1
        else:
            occ[animal] = 1
    
    animals = list(occ.keys())
    animals.sort()
    
    print("List " + str(case) + ":")
    
    for a in animals:
        print(a + " | " + str(occ[a]))
    
    case += 1
    n = int(input())