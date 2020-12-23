class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = {}
        for index, value in enumerate(s):
            if value in result:
                result[value] = -1
            else:
                result[value] = index

        res = len(s)
        for item in result.values():
            if res > item >= 0:
                res = item
        return res if res != len(s) else -1
