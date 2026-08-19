class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        l,r = 0,1
        cur = 1
        best = 1

        while r < n:
            if arr[r] == arr[r-1]:
                l = r
                r += 1

            elif r-l == 1:
                r += 1

            elif arr[r] > arr[r-1]:
                if arr[r-1] > arr[r-2]:
                    l = r-1
                r += 1
            
            else:
                if arr[r-1] < arr[r-2]:
                    l = r-1
                r += 1

            cur = r-l
            best = max(best, cur)
        
        return best