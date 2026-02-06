# LeetCode 647. Palindromic Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            left = i - 1
            right = i + 1
            count += 1
            while right < n and s[right] == s[i]:
                count += 1
                right += 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count