class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        dp = [1] * l
        parent = [-1] * l

        for i in range(l-2, -1, -1):
            for j in range(i+1, l):
                if nums[j] % nums[i] == 0:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        parent[i] = j
        
        indexMax = 0

        for i in range(l):
            if dp[i] > dp[indexMax]:
                indexMax = i
        
        ind = [indexMax]

        while parent[ind[-1]] != -1:
            ind.append(parent[ind[-1]])
        
        ans = []

        for i in ind:
            ans.append(nums[i])

        return ans