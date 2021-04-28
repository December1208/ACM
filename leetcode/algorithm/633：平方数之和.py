import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        r, l = 0, int(math.sqrt(c))
        while r <= l:
            if r * r + l * l == c:
                return True
            elif r * r + l * l < c:
                r += 1
            elif r * r + l * l > c:
                l -= 1
        return False
