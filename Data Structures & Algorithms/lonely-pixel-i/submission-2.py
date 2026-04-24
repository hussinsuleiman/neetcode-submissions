class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n, m = len(picture), len(picture[0])
        rows = [[] for i in range(n)]
        cols = [[] for i in range(m)]
        t = 0

        for i in range(n):
            for j in range(m):
                if picture[i][j] == 'B':
                    rows[i].append(j)
                    cols[j].append(i)

        for i in range(n):
            if len(rows[i]) == 1 and len(cols[rows[i][0]]) == 1:
                t += 1            

        return t