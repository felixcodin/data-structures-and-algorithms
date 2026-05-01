# LeetCode 1386. Cinema Seat Allocation


from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        left = {2, 3, 4, 5}
        mid = {4, 5, 6, 7}
        right = {6, 7, 8 , 9}

        reservedSeatsMap = defaultdict(list)
        for r, c in reservedSeats:
            reservedSeatsMap[r].append(c)

        result = n * 2
        for _, seats in reservedSeatsMap.items():
            validLeft = True
            validMid = True
            validRight = True
            for seat in seats:
                if seat in left:
                    validLeft = False
                if seat in mid:
                    validMid = False
                if seat in right:
                    validRight = False
            if not validLeft and not validRight and not validMid:
                result -= 2
            elif not validLeft or not validRight:
                result -= 1
                
        return result