class Solution:
    """
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
    动态规划
    若s[i:j]是回文串，那么s[i+1:j-1]也一定是回文串
    """
    def longestPalindrome(self, s: str) -> str:
        s_length = len(s)
        ans = ""
        dp = [[False] * s_length for _ in range(s_length)]
        for length in range(s_length):
            for left in range(s_length):
                right = left + length
                if right >= s_length:
                    break
                if length == 0:
                    dp[left][right] = True
                elif length == 1:
                    dp[left][right] = (s[left] == s[right])
                else:
                    dp[left][right] = (dp[left + 1][right - 1] and s[left] == s[right])
                if dp[left][right] and length + 1 > len(ans):
                    ans = s[left:right + 1]
        return ans

    def Palindrome(self, s: str) -> bool:
        """
        判断一个字符串是否是回文串
        :param s:
        :return:
        """
        s_length = len(s)
        if s_length == 1:
            return True
        s_mid = s_length // 2
        for i in range(s_mid+1):
            left = s_mid - i
            right = s_mid + i
            if s[left] != s[right]:
                return False
        return True


print(Solution().longestPalindrome("abc"))
