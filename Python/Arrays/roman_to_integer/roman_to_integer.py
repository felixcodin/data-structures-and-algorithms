class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        romanDict = {'M': 1000, 'D': 500,
                     'C': 100, 'L': 50,
                     'X': 10, 'V':  5,
                     'I': 1}

        prev = 0
        for char in s[::-1]:
            current = romanDict[char]
            if prev > current:
                res -= current
            else:
                res += current
                prev = current
        
        return res