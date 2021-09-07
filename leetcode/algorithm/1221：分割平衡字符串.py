class Solution:
    def balancedStringSplit(self, s: str) -> int:

        result, d = 0, 0
        for char in s:
            if char == 'L':
                d += 1
            else:
                d -= 1

            if d == 0:
                result += 1

        return result


if __name__ == '__main__':

    solution = Solution()
    print(solution.balancedStringSplit('RLRLRLRLRLRLRL'))
    print(solution.balancedStringSplit('LLLRRRLLRLR'))
