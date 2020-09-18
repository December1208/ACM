import copy
from typing import List


class Solution:
    """
        回溯+剪枝
        首先先按照没有重复数字时进行全排列，然后再对于重复的数字进行剪枝
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        nums_length = len(nums)
        vis = {index: 0 for index in range(nums_length)}
        temp_result: List[int] = []
        result: List[List[int]] = []


        def arrangement(n: int):
            if n == nums_length:
                result.append(copy.deepcopy(temp_result))
                return
            for index, num in enumerate(nums):
                if vis[index] == 1:
                    continue
                if index > 0 and num == nums[index-1] and vis[index-1] == 0:
                    continue
                temp_result.append(num)
                vis[index] = 1
                arrangement(n+1)
                temp_result.pop()
                vis[index] = 0
        arrangement(0)
        return result


print(Solution().permuteUnique([1, 1, 3]))
