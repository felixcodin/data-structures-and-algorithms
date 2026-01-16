# LeetCode 424. Longest Repeating Character Replacement

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        right = 0
        maxFreq = 0
        while right < len(s):
            freq[s[right]] += 1
            maxFreq = max(maxFreq, freq[s[right]])
            while right - left + 1 - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            right += 1
        return right - left