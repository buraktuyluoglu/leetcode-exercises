class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        num = abs(x)
        reversed_num = 0

        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10

        if reversed_num > 2**31 - 1:
            return 0
            
        return sign * reversed_num