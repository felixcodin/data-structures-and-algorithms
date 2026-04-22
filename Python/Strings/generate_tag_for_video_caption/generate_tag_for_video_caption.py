# Leetcode 3582. Generate Tag for Video Caption

class Solution:
    def generateTag(self, caption: str) -> str:
        caption = "".join(caption.title().split())
        
        caption = caption[0].lower() + caption[1:] if caption else ""

        return '#' + caption[:99]
