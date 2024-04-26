class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        sign = 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit
            i += 1
            
        result *= sign
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if result > INT_MAX:
            return INT_MAX

        elif result < INT_MIN:
            return INT_MIN

        else:
            return result
