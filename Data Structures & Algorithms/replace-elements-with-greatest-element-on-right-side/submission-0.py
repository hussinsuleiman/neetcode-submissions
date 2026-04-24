class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        output = [-1] * n
        m = arr[-1]

        for i in range(n-2, -1, -1):
            output[i] = m
            m = max(m, arr[i])
        
        return output
        