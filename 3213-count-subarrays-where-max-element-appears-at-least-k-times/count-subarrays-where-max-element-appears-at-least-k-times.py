class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_value = max(nums)
        output = 0
        left = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] == max_value:
                count += 1
            while count >= k:
                if nums[left] == max_value:
                    count -= 1
                left += 1
            output += left
        return output