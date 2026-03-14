# LeetCode 933. Number of Recent Calls

from collections import deque


class RecentCounter:

    def __init__(self):
        self.recentCounter = deque()

    def ping(self, t: int) -> int:
        self.recentCounter.append(t)
        
        while self.recentCounter:
            if self.recentCounter[0] < t - 3000:
                self.recentCounter.popleft()
            else:
                break

        return len(self.recentCounter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)