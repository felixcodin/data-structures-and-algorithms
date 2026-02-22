# LeetCode 605. Can Place Flowers

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        m = len(flowerbed)

        for i in range(m):
            cur = flowerbed[i]
            nxt = 0 if i + 1 >= m else flowerbed[i + 1]
            if prev == cur == nxt == 0:
                n -= 1
                flowerbed[i] = 1
                cur = 1
            prev = cur

        return n <= 0