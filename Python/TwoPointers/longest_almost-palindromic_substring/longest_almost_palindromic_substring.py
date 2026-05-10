# 3844. Longest Almost-Palindromic Substring

class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        res = 0

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            nonlocal res
            res = max(res, right - left - 1)
            return left, right
        
        for i in range(2*n-1):
            left, right = expand(i//2, (i+1)//2)
            expand(left - 1, right)
            expand(left, right + 1)
            
        return min(res, n)