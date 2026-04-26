# LeetCode 2075. Decode the Slanted Ciphertext

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        if rows == 1:
            return encodedText
        
        columns = n // rows
        step = columns + 1
        start_index = 0
        cur = 0
        res = []
        while start_index < columns:
            res.append(encodedText[cur])
            cur += step
            if cur >= n:
                start_index += 1
                cur = start_index
        
        return "".join(res).rstrip()
