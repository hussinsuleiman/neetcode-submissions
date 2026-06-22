class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        a = []

        for i in range(1, m):
            a.append(set(mat[i]))
        
        for i in mat[0]:
            valid = True

            for s in a:
                if i not in s:
                    valid = False
                    break
            
            if valid:
                return i
        
        return -1