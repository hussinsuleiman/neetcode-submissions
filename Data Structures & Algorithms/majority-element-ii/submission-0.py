class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dico = dict()
        l = len(nums)

        for n in nums:
            if n in dico.keys():
                dico[n] += 1
            elif len(dico.keys()) < 2:
                dico[n] = 1
            else:
                for key in list(dico.keys()):
                    if dico[key] == 1:
                        del dico[key]
                    else:
                        dico[key] -= 1
        
        occ = dict()

        for elt in dico:
            occ[elt] = 0
        
        for n in nums:
            if n in occ.keys():
                occ[n] += 1

        output = []

        for elt in occ.keys():
            if occ[elt] > l // 3:
                output.append(elt)

        return output 