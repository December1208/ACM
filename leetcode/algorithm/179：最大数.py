from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        self.quick_sort(nums=nums, l=0, r=len(nums) - 1)
        if nums[0] == '0':
            return '0'
        return ''.join(nums)

    def quick_sort(self, nums: List[str], l, r):
        i, j = l, r
        if i>=j:
            return
        num = nums[l]
        while i < j:
            while i < j and int(nums[j] + num) <= int(num + nums[j]):
                j -= 1
            while i < j and int(nums[i] + num) >= int(num + nums[i]):
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[l], nums[i] = nums[i], num
        self.quick_sort(nums, l, i-1)
        self.quick_sort(nums, i+1, r)


if __name__ == '__main__':
    print(Solution().largestNumber([10, 2]))
