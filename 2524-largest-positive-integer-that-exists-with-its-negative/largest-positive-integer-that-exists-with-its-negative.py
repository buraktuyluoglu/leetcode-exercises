class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        odds = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] * -1:
                    odds.append(nums[i])

        if len(odds) > 0:
            return abs(odds[0])
        else:
            return -1
                    
            
        