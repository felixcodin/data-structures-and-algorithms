class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        
        result = 0
        is_word = False
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i].isspace() and is_word:
                break
            if not s[i].isspace():
                is_word = True
                result += 1
            else:
                is_word = False
        
        return result