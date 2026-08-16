class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, 111*int(num[i]))
        
        if res == 0:
            return '000'

        return str(res) if res > -1 else ''