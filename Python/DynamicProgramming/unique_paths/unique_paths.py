# LeetCode 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for w in range(m):
            for i in range(n):
                if w - 1 >= 0:
                    dp[w][i] += dp[w-1][i]
                if i - 1 >= 0:
                    dp[w][i] += dp[w][i-1]

        return dp[m-1][n-1]