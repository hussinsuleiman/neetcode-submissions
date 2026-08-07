class CountSquares:
    def __init__(self):
        self.mat = [[0]*1001 for i in range(1001)]

    def add(self, point: List[int]) -> None:
        self.mat[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        x,y = point[0], point[1]
        tot = 0

        for i in range(x+y+1):
            if i == x:
                continue

            if max(i, x+y-i) > 1000:
                continue

            tot += self.mat[i][x+y-i] * self.mat[i][y] * self.mat[x][x+y-i]

        for i in range(x - min(x,y), 1001):
            if i == x:
                continue
            
            if i-x+y > 1000:
                break

            tot += self.mat[i][i-x+y] * self.mat[i][y] * self.mat[x][i-x+y]

        return tot