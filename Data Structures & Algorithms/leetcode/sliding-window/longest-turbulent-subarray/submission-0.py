class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = len(arr)
        i = 0
        res = 1

        while i < l-1:
            while i < l-1 and arr[i+1] == arr[i]:
                i += 1

            if i >= l-1:
                return res

            inc = (arr[i+1]-arr[i] > 0)
            i += 1
            cur = 2

            while i < l-1 and ((arr[i+1]-arr[i] < 0 and inc) or (arr[i+1]-arr[i] > 0 and not inc)):
                i += 1
                cur += 1
                inc = not inc

            res = max(res, cur)

        return res 