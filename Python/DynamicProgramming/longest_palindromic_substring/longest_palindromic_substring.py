# LeetCode 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        for i in range(n):
            cur = s[i]
            left = i - 1
            right = i + 1
            while right < n and s[right] == s[i]:
                right += 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len(res):
                res = s[left+1:right]

        return res