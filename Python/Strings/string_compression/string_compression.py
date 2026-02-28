# LeetCode 443. String Compression

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0

        n = len(chars)
        while right < n:
            prev = chars[right]
            count = 0
            while right < n and chars[right] == prev:
                right += 1
                count += 1
            
            chars[left] = prev
            left += 1
            if count > 1:
                for c in str(count):
                    chars[left] = c
                    left += 1

        return left