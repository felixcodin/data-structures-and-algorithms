# LeetCode 139. Word Break

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        l = len(max(wordDict, key=len))
        word_set = set(wordDict)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n + 1):
            for j in range(max(0, i-l), i):
                if dp[j] == True and s[j:i] in word_set:
                    dp[i] = True
        
        return dp[n]