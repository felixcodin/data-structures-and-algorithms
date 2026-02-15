# LeetCode 567. Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if m < n:
            return False

        need = [0 for _ in range(26)]
        window = [0 for _ in range(26)]

        for i in range(n):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        matches = 0

        for i in range(26):
            if window[i] == need[i]:
                matches += 1


        left = 1
        right = n
        while right < m:
            if matches == 26:
                return True
                
            prev = ord(s2[left-1]) - ord('a')
            if window[prev] == need[prev]:
                matches -= 1
            elif window[prev] - 1 == need[prev]:
                matches += 1
            window[prev] -= 1
            
            cur = ord(s2[right]) - ord('a')
            if window[cur] + 1 == need[cur]:
                matches += 1
            elif window[cur] == need[cur]:
                matches -= 1
            window[cur] += 1

            left += 1
            right += 1
        
        return matches == 26