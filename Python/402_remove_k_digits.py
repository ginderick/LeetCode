class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for char in num:

            while k > 0 and stack and stack[-1] > char:
                k -= 1
                stack.pop()
            stack.append(char)

        if k > 0:
            while k > 0:
                stack.pop()
                k -= 1

        result = "".join(stack)
        if result:
            return str(int(result))
        else:
            return "0"


sol = Solution()
num = "12355"
k = 3
result = sol.removeKdigits(num, k)
print(result)
