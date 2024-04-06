class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        # Kaldırılacak indeksleri belirle
        indices_to_remove = set(stack)

        # Kaldırılacak parantezleri çıkar
        result = ""
        for i, char in enumerate(s):
            if i not in indices_to_remove:
                result += char

        return result
