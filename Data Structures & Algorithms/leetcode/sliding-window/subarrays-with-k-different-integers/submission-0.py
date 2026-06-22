class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(t):
            count = defaultdict(int)
            left = 0
            ans = 0
            distinct = 0

            for right, x in enumerate(nums):
                if count[x] == 0:
                    distinct += 1

                count[x] += 1

                while distinct > t:
                    y = nums[left]
                    count[y] -= 1
                    
                    if count[y] == 0:
                        distinct -= 1
                    
                    left += 1
                
                ans += right-left+1
            
            return ans

        return at_most(k) - at_most(k-1)