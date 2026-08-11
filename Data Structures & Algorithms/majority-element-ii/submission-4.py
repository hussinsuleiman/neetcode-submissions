class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occ = defaultdict(int)
        l = 0
        res = []
        t = len(nums)

        for n in nums:
            if n not in occ and l == 2:
                keys = occ.keys()

                for key in list(keys):
                    occ[key] -= 1

                    if occ[key] == 0:
                        del occ[key]
                        l -= 1

            else:
                if n not in occ:
                    l += 1

                occ[n] += 1

        tot = defaultdict(int)

        for key in occ:
            for n in nums:
                if n == key:
                    tot[key] += 1

        for key in tot:
            if tot[key] > t//3:
                res.append(key)
        
        return res