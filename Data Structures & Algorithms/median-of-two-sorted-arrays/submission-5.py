class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,l2 = len(nums1), len(nums2)

        if l1 > l2:
            nums1, nums2 = nums2, nums1
            l1, l2 = l2, l1
        
        if not nums1:
            if l2%2 == 1:
                return nums2[l2//2]
            else:
                return (nums2[l2//2] + nums2[l2//2-1]) / 2

        INF = float('inf')
        l,r = 0,l1

        while l <= r:
            mid = (l+r)//2
            left1, right1 = 0,0

            if mid == 0:
                left1 = -INF
                right1 = nums1[0]
            elif mid == l1:
                left1 = nums1[-1]
                right1 = INF
            else:
                left1 = nums1[mid-1]
                right1 = nums1[mid]

            left2, right2 = 0,0 

            if (l1+l2) // 2 - mid == 0:
                left2 = -INF
                right2 = nums2[(l1+l2) // 2 - mid]
            elif (l1+l2) // 2 - mid == l2:
                left2 = nums2[-1]
                right2 = INF
            else:
                left2 = nums2[(l1+l2) // 2 - mid-1]
                right2 = nums2[(l1+l2) // 2 - mid]

            if left1 > right2:
                r = mid-1
            elif right1 < left2:
                l = mid+1
            else:
                if (l1+l2)%2 == 1:
                    return min(right2, right1)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2