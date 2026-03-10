# LeetCode 1657. Determine if Two Strings Are Close

from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        chars1 = defaultdict(int)
        for char in word1:
            chars1[char] += 1

        chars2 = defaultdict(int)
        for char in word2:
            if char not in chars1:
                return False
            chars2[char] += 1

        if len(chars1) != len(chars2):
            return False
        
        freq_map = defaultdict(int)
        for _, value in chars1.items():
            freq_map[value] += 1
        for _, value in chars2.items():
            freq_map[value] -= 1

        for _, value in freq_map.items():
            if value != 0:
                return False

        return True