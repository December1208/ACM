from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':

    s = Solution()
    print(s.peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))
