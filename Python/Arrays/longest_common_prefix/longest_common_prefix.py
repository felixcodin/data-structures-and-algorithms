# LeetCode 14. Longest Common Prefix

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = []
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if i >= len(strs[j]) or c != strs[j][i]:
                    return "".join(prefix)
            prefix.append(c)

        return "".join(prefix)