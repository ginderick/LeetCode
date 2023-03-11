class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


class Solution_2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        return x == self.reverseUtil(x)

    def reverseUtil(self, x: int):
        result = 0

        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = int(x / 10)

        return result
