# LeetCode 1207. Unique Number of Occurrences

from collections import defaultdict
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = defaultdict(int)

        for num in arr:
            mp[num] += 1
        
        st = set()
        for key, value in mp.items():
            if value in st:
                return False
            st.add(value)

        return True