class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        l = len(arr)
        d = (arr[-1]-arr[0]) // l
        
        for i in range(l):
            if arr[i] != arr[0] + d*i:
                return arr[0] + d*i
        
        return arr[0] + d*l