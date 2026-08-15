class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = arr[-1]
        arr[-1] = -1

        for i in range(-2, -len(arr)-1, -1):
            temp = max(arr[i], m)
            arr[i] = m
            m = temp
        
        return arr