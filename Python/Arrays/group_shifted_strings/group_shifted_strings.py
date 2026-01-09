# LeetCode 249. Group Shifted Strings

from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings:
            return []

        res = []
        hash_map = defaultdict(list)
        for string in strings:
            shift = (ord(string[0]) - ord('a') + 26) % 26
            key = (((ord(string[0]) - ord('a') + 26) - shift) % 26,)
            for i in range(1, len(string)):
                key = key + (((ord(string[i]) - ord('a') + 26)  - shift) % 26,)
            hash_map[key].append(string)

        for key, value in hash_map.items():
            res.append(value)

        return res