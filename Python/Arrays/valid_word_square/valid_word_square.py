# LeetCode 422. Valid Word Square

from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words:
            return True
        if len(words) != len(words[0]):
            return False

        for i in range(len(words)):
            for j in range(len(words[i])):
                if (
                    j >= len(words)
                    or i >= len(words[j])
                    or words[i][j] != words[j][i]
                ):
                    return False

        return True