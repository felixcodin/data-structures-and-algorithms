# LeetCode 2486. Append Characters to String to Make Subsequence

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if not s and t:
            return len(t)
        if s and not t:
            return 0

        i = 0
        n = len(t)

        for c in s:
            if i == n:
                break
            if c == t[i]:
                i += 1

        return n - i