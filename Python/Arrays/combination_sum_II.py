#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#Each number in candidates may only be used once in the combination.
#Note: The solution set must not contain duplicate combinations.

def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def backtrack(start, current_combination, current_sum):
        if current_sum > target:
            return
        if current_sum == target:
            res.append(current_combination[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            current_combination.append(candidates[i])
            backtrack(i + 1, current_combination, current_sum + candidates[i])
            current_combination.pop()

    backtrack(0, [], 0)
    return res