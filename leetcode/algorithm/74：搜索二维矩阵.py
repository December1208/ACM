from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row_index = self.binary_search_column(matrix, target)
        print(row_index)
        if row_index < 0:
            return False

        return self.binary_search_row(matrix[row_index], target)

    def binary_search_row(self, matrix: List[int], target):
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (right + left) // 2
            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                left = mid + 1
            elif matrix[mid] > target:
                right = mid - 1
        return False

    def binary_search_column(self, matrix: List[List[int]], target):
        left, right = -1, len(matrix) - 1

        while left < right:

            mid = (right + left + 1) // 2
            if matrix[mid][0] <= target:
                left = mid
            else:
                right = mid - 1

        return left


if __name__ == '__main__':

    print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(Solution().searchMatrix([[1]], 1))
    print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
