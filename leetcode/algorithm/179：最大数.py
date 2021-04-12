from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self.quick_sort(nums=nums, l=0, r=len(nums) - 1)
        nums = [str(num) for num in nums]
        return ''.join(nums)

    def quick_sort(self, nums: List[int], l, r):
        num = nums[l]
        i, j = l, r
        if i>=j:
            return
        while i < j:
            while i < j and int(str(nums[j]) + str(num)) <= int(str(num) + str(nums[j])):
                j -= 1
            while i < j and int(str(nums[i]) + str(num)) >= int(str(num) + str(nums[i])):
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[l] = nums[i]
        nums[i] = num
        self.quick_sort(nums, l, i-1)
        self.quick_sort(nums, i+1, r)


if __name__ == '__main__':
    print(Solution().largestNumber([10, 2]))
