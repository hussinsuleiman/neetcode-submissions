class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        l = 0
        r = len(A)-1
        half = (len(A)+len(B)) // 2

        while True:
            mid = (l+r) // 2
            
            ALeft = A[mid] if mid >= 0 else float('-inf')
            Aright = A[mid+1] if mid+1 < len(A) else float('inf')
            BLeft = B[half-mid-2] if half-mid-2 >= 0 else float('-inf') 
            Bright = B[half-mid-1] if half-mid-1 < len(B) else float('inf')

            if ALeft <= Bright and BLeft <= Aright:
                if (len(A)+len(B)) % 2 == 0:
                    return (min(Bright, Aright) + max(BLeft, ALeft)) / 2
                else:
                    return min(Aright, Bright)
            
            elif ALeft > Bright:
                r = mid-1
            else:
                l = mid+1


