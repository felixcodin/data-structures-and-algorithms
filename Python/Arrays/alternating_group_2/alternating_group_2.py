#There is a circle of red and blue tiles. You are given an array of integers 'colors' and an integer 'k'. The color of tile 'i' is represented by 'colors[i]':
#`colors[i] == 0` means that tile i is red.
#`colors[i] == 1` means taht tile i is blue.

class Solution:
    def numberOfAlternatingGroup(self, colors, k):
        n = len(colors)
        if k > n:
            return 0
                
        res = 0
        count = 0

        for i in range(k - 1):
            if colors[i] != colors[i + 1]:
                count += 1
        
        if count == k - 1:
            res += 1

        for i in range(1, n):
            if colors[i - 1] != colors[i % n]:
                count -= 1
            if colors[(i - 2 + k) % n] != colors[(i - 1 + k) % n]:
                count += 1
            if count == k - 1:
                res += 1

        return res

sol = Solution()
print(sol.numberOfAlternatingGroup([0,1,0,0,1,0,1], 6))