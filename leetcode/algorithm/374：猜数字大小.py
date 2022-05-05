pick = 6


def guess(num) -> int:
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            num = (left + right) // 2
            res = guess(num)

            if res == 0:
                return num
            elif res == -1:
                right = num - 1
            else:
                left = num + 1


if __name__ == '__main__':
    print(Solution().guessNumber(10))
