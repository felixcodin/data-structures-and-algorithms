#Given a string s consisting only of characters a, b and c.
#Return the number of substrings containing at least one occurrence of all these characters a, b and c.

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        arr = [-1, -1, -1]

        for i in range(len(s)):
            char = s[i]
            arr[ord(char) - ord('a')] = i
            count += 1 + min(arr)

        return count