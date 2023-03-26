class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) + 1 - len(needle)):

            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
            # if needle == (haystack[i : (i + needle_len)]):
            #     return i

        return -1


sol = Solution()
haystack = "hello"
needle = "ll"
result = sol.strStr(haystack, needle)
print(result)
