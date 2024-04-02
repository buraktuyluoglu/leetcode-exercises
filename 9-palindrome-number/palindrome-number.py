class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = str(x)
        return l == l[::-1]
            

