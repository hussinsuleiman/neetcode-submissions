class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i,j = 0,k-1
        s = 0
        l = len(arr)
        res = 0

        for a in range(k):
            s += arr[a]
        
        while j < l:
            if s >= k*threshold:
                res += 1
            
            j += 1

            if j < l:
                s = s-arr[i]+arr[j]
                i += 1
        
        return res