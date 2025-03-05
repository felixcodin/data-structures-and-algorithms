#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#Each number in candidates may only be used once in the combination.
#Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()

        def backtrack(start, current_combination, current_sum):
            if current_sum == target:
                result.append(current_combination[:])
                return
            if current_sum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                current_combination.append(candidates[i])
                backtrack(i + 1, current_combination, current_sum + candidates[i])
                current_combination.pop()
        
        backtrack(0, [], 0)
        return result
            