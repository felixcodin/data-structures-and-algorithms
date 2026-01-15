class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        
        last = {}
        left = 0
        for right, c in enumerate(s):
            if c in last and last[c] >= left:
                left = last[c] + 1
            last[c] = right
            res = max(res, right - left + 1)

        return res