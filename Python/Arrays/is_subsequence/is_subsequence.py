class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and t:
            return True
        if s and not t:
            return False
        
        n = len(s)
        i = 0
        for c in t:
            if i == n:
                break
            if s[i] == c:
                i += 1
        
        return i == n