class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize a 2D DP table to store the results of subproblems
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Empty string and empty pattern always match
        dp[0][0] = True

        # Handle patterns like "a*", "b*", etc. (match zero characters)
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # Case 1: Characters match or pattern is '.'
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # Case 2: Pattern is '*'
                elif p[j - 1] == '*':
                    # '*' matches zero or one preceding character
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == '.' or p[j - 2] == s[i - 1]))
                # Case 3: Characters don't match
                else:
                    dp[i][j] = False

        # Return the result for the entire string
        return dp[len(s)][len(p)]