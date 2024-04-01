from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, target, [], result)
        return result
    
    def backtrack(self, candidates, target, current, result):
        if target < 0:
            return
        elif target == 0:
            result.append(current)
            return
        for i, candidate in enumerate(candidates):
            self.backtrack(candidates[i:], target - candidate, current + [candidate], result)

# Test
solution = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(solution.combinationSum(candidates, target))
