class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(n-1, 1, -1):  # i = en büyük kenarın indeksi
            left = 0                # küçük kenar pointer
            right = i - 1           # orta kenar pointer

            # İki-pointer ile diğer iki kenarı bul
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    # Geçerli üçgen: left ile right arasındaki tüm sayılar
                    result += (right - left)
                    right -= 1  # orta kenarı küçült
                else:
                    left += 1   # küçük kenarı büyüt

        return result