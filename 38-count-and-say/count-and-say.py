class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            result = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(result))
        return result
