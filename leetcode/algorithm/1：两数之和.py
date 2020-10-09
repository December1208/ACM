from typing import List


class Solution:
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}
        for index, value in enumerate(nums):
            if target - value in temp_dict:
                return [temp_dict[target-value], index]
            temp_dict.update({value: index})
        return []
