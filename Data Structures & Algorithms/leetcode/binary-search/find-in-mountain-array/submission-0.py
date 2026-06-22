class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]
        
        left, right = 0, n-1

        while left < right:
            mid = (left + right) // 2

            if get(mid) < get(mid+1):
                left = mid+1
            else:
                right = mid
        
        peak = left

        left, right = 0, peak

        while left <= right:
            mid = (left + right) // 2
            val = get(mid)

            if val == target:
                return mid
            elif val < target:
                left = mid+1
            else:
                right = mid-1
        
        left, right = peak+1, n-1

        while left <= right:
            mid = (left + right) // 2
            val = get(mid)

            if val == target:
                return mid
            elif val < target:
                right = mid-1
            else:
                left = mid+1 

        return -1