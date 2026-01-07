# LeetCode 2115. Find All Possible Recipes from Given Supplies

from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        need_count = []
        waiting = defaultdict(list)
        res = []
        supplies = set(supplies)
        for i in range(len(ingredients)):
            count = 0
            for item in ingredients[i]:
                waiting[item].append(i)
                if item not in supplies:
                    count += 1
            need_count.append(count)

        queue = deque()
        for i in range(len(need_count)):
            if need_count[i] == 0:
                queue.append(i)
                res.append(recipes[i])

        while queue:
            curr = queue.popleft()
            if recipes[curr] not in waiting:
                continue
            for item in waiting[recipes[curr]]:
                need_count[item] -= 1
                if need_count[item] == 0:
                    queue.append(item)
                    res.append(recipes[item])

        return res
