class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)

        if s%k != 0 or max(nums) > s//k:
            return False
        
        sub = defaultdict(int)
        sub[0] = k
        nums.sort()
        n = len(nums)

        def backtrack(i):
            if i < 0:
                return sub[s//k] == k

            for x in list(sub.keys()):
                if sub[x] > 0 and x + nums[i] <= s//k:
                    sub[x] -= 1
                    sub[x + nums[i]] += 1
                    ans = backtrack(i-1)

                    if ans:
                        return True
                    
                    sub[x] += 1
                    sub[x + nums[i]] -= 1

            return False

        return backtrack(n-1)