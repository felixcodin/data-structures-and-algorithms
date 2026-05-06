# LeetCode 375. Guess Number Higher or Lower II

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for length in range(2, n + 1):
            for left in range(1, n - length + 2):
                right = left + length - 1
                dp[left][right] = float('inf')
                for k in range(left, right + 1):
                    l = dp[left][k-1] if k > left else 0
                    r = dp[k+1][right] if k < right else 0
                    cost = k + max(l, r)
                    if (dp[left][right] > cost):
                        dp[left][right] = cost
        
        return dp[1][n]