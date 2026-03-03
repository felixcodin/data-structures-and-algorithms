# LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0

        left = 0
        right = 0
        window = 0
        while right < k:
            if s[right] in vowels:
                window += 1
            right += 1
        
        res = window
        while right < len(s):
            if s[left] in vowels:
                window -= 1
            if s[right] in vowels:
                window += 1
            left += 1
            right += 1
            res = max(res, window)
        
        return res