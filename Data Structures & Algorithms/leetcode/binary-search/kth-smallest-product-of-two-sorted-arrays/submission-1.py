class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)

        def upper_bound(arr: List[int], x: int) -> int:
            left, right = 0, len(arr)

            while left < right:
                mid = (left + right) // 2

                if arr[mid] <= x:
                    left = mid + 1
                else:
                    right = mid

            return left

        def lower_bound(arr: List[int], x: int) -> int:
            left, right = 0, len(arr)

            while left < right:
                mid = (left + right) // 2

                if arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid

            return left

        def ceil_div(a: int, b: int) -> int:
            q = a // b

            if a % b == 0:
                return q

            return q + 1

        def countPairs(t: int) -> int:
            count = 0

            for x in nums1:
                if x > 0:
                    bound = t // x
                    count += upper_bound(nums2, bound)

                elif x < 0:
                    bound = ceil_div(t, x)
                    count += m - lower_bound(nums2, bound)

                else:
                    if t >= 0:
                        count += m

            return count

        candidates = [nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1]]
        left, right = min(candidates), max(candidates)

        while left < right:
            mid = (left + right) // 2

            if countPairs(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left