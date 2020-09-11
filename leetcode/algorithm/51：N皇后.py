from typing import List


class Solution:
    """
    执行用时：52 ms, 在所有 Python3 提交中击败了97.02%的用户
    内存消耗：13.9 MB, 在所有 Python3 提交中击败了77.56%的用户
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens_map = [0] * n
        result: List[List[str]] = []
        column = [False] * n
        main = [False] * (2*n-1)
        deputy = [False] * (2*n-1)

        def dfs(temp: int):
            if temp >= n > 0:
                append_result()
            else:
                for value in range(n):
                    if main[temp-value+n-1] or deputy[temp+value] or column[value]:
                        continue
                    queens_map[temp] = value
                    main[temp-value+n-1] = True
                    deputy[temp+value] = True
                    column[value] = True
                    dfs(temp + 1)
                    main[temp-value+n-1] = False
                    deputy[temp+value] = False
                    column[value] = False

        def append_result():
            result.append(
                [
                    ''.join(
                        ['.' for j in range(queens_map[i])] + ['Q'] + ['.' for j in range(queens_map[i] + 1, n)]
                    )
                    for i in range(n)
                ]
            )

        dfs(0)
        return result

Solution().solveNQueens(12)
