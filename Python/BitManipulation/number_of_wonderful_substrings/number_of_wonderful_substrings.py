# LeetCode 1915. Number of Wonderful Substrings

from collections import defaultdict


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        res = 0

        count = defaultdict(int)
        count[0] = 1
        mask = 0
        for ch in word:
            bit = ord(ch) - ord('a')
            mask ^= (1 << bit)

            res += count[mask]

            for i in range(10):
                res += count[mask ^ (1 << i)]
            
            count[mask] += 1


        return res