# LeetCode 649. Dota2 Senate

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire_queue = deque()
        radiant_queue = deque()

        for i,senator in enumerate(senate):
            if senator == "R":
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        n = len(senate)
        while dire_queue and radiant_queue:
            r = radiant_queue.popleft()
            d = dire_queue.popleft()

            if r < d:
                radiant_queue.append(r + n)
            else:
                dire_queue.append(d + n)
        
        return "Radiant" if radiant_queue else "Dire"