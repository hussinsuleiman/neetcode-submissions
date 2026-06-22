N = int(input())
potentials = []

for i in range(N):
    line = list(map(int, input().split())) 
    potentials.append(line)

maxDrama = 0
maxIndices = (0, 0, 0)

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            drama = potentials[i][j] * potentials[i][k] * potentials[j][k]
            
            if drama > maxDrama:
                maxDrama = drama
                maxIndices = (i, j, k)

print(maxIndices[0] + 1, maxIndices[1] + 1, maxIndices[2] + 1)