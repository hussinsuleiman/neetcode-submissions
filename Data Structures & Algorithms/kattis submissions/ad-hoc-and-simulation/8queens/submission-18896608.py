queens = []
done = False

for i in range(8):
    line = input()
    
    for j in range(8):
        if line[j] == '*':
            for a,b in queens:
                if i == a or j == b or a-i == b-j or a-i == j-b:
                    print("invalid")
                    done = True
                    break
            
            if done:
                break
                
            queens.append((i,j))
    
    if done:
        break

if not done:
    if len(queens) == 8:
        print("valid")
    else:
        print("invalid")