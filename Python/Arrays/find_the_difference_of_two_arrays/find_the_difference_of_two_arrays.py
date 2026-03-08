# LeetCode 2215. Find the Difference of Two Arrays

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        mp = {}

        for num in nums1:
            mp[num] = True
        
        res2 = set()
        for num in nums2:
            if num in mp:
                mp[num] = False
            else:
                res2.add(num)
        
        res1 = []
        for key, value in mp.items():
            if value:
                res1.append(key)

        return [res1, list(res2)]