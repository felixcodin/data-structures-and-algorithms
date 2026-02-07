# LeetCode 91. Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        p = [1, 0]
        prev = ""
        for c in s:
            count = 0
            if 0 < int(c) <= 26:
                count += p[0]
            if prev != '0' and 0 < int(prev + c) <= 26:
                count += p[1]
            prev = c
            p[1] = p[0]
            p[0] = count
        return p[0]
