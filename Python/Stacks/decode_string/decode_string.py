# LeetCode 394. Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        k = 0
        stack = []
        for c in s:
            if c.isdigit():
                k *= 10
                k += int(c)
            elif c == '[':
                stack.append((res, k))
                k = 0
                res = ""
            elif c == ']':
                curr = stack.pop()
                res = curr[0] + res*curr[1]
            else:
                res += c

        return res