# LeetCode 151. Reverse Words in a String

#####  Use `split` func
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])
    
#####  Not use `split` func  #####
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)

        words = []
        i = 0
        while i < n:
            while i < n and s[i].isspace():
                i += 1
            j = i
            while i < n and not s[i].isspace():
                i += 1
            if i > j:
                words.append(s[j:i])
        
        return " ".join(words[::-1])
"""