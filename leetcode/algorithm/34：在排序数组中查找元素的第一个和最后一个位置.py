from typing import List


class Solution:

    def binary_search(self, nums: List[int], target: int, lower: bool):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > target or (lower and nums[mid] >= target):
                right = mid - 1
            else:
                left = mid + 1
        res = -1
        if lower and left < len(nums) and nums[left] == target:
            res = left
        elif not lower and right >= 0 and nums[right] == target:
            res = right

        return res

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [
            self.binary_search(nums, target, True),
            self.binary_search(nums, target, False)
        ]
        return res


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
