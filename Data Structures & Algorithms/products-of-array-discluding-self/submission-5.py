class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        nbZeroes = 0

        for n in nums:
            if n == 0:
                nbZeroes += 1
            else:
                p *= n
        
        res = []

        for n in nums:
            if nbZeroes > 1:
                res.append(0)
                
            elif nbZeroes == 1:
                if n == 0:
                    res.append(p)
                else:
                    res.append(0)

            else:
                res.append(p//n)
        
        return res