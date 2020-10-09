from typing import List
import copy


class Solution:
    """
    找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        temp = []
        def dfs(current: int, end: int, temp_size: int, list_sum: int):

            if len(temp) + (end-current+1) < temp_size or len(temp) > temp_size or sum(temp) > list_sum:
                return

            if len(temp) == temp_size and sum(temp) == list_sum:
                result.append(copy.copy(temp))
                return
            temp.append(current)
            dfs(current+1, end, temp_size, list_sum)
            temp.pop()
            dfs(current+1, end, temp_size, list_sum)
        dfs(1, 9, k, n)
        return result


print(Solution().combinationSum3(3, 9))
