from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        current_sum = 0

        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_sub = max(max_sub, current_sum)

        return max_sub


sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = sol.maxSubArray(nums)
print(result)
