class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        char_dict = {"}": "{", "]": "[", ")": "("}

        for i in s:
            if not stack:
                stack.append(i)
                continue
            if char_dict.get(i) == stack[-1]:
                stack.pop()
                continue
            else:
                stack.append(i)

        return True if not stack else False


sol = Solution()
result = sol.isValid("([)]")
print(result)
