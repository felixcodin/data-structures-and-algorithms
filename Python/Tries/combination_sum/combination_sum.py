# LeetCode 39. Combination Sum

from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return []
        
        res = []
        nums = sorted(set(nums))

        def dfs(index, note, curr_sum):
            if curr_sum == target:
                res.append(note[:])
                return
            if curr_sum > target or index >= len(nums):
                return
            note.append(nums[index])
            dfs(index, note, curr_sum + nums[index])
            note.pop()
            dfs(index + 1, note, curr_sum)

        dfs(0, [], 0)
        return res

