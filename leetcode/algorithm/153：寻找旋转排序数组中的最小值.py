from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r - 1]:
                r = mid
            else:
                l = mid + 1

        return nums[l]
