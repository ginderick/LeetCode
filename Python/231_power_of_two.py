class Solution:
    # O(logn)
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 2 != 0 or n == 0:
            return False

        return self.isPowerOfTwo(n / 2)

    # O(1)
    def isPowerOfTwoSolTwo(self, n):
        if (n > 0) and (n & (n - 1) == 0):
            return True
        else:
            return False


# Driver code

sol = Solution()
answer = sol.isPowerOfTwo(16)
print(answer)
