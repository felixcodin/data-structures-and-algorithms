# LeetCode 2390. Removing Stars From a String

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and c == '*':
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)