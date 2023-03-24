from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right

            right += 1
        return max_profit


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = sol.maxProfit(prices)
