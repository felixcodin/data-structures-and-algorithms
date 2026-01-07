# LeetCode 2678. Number of Senior Citizens

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0

        for word in details:
            age = word[11] + word[12]
            if int(age) > 60:
                result += 1

        return result