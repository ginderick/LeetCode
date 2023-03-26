from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            if target == nums[middle_pointer]:
                return middle_pointer

            if target > nums[middle_pointer]:
                left_pointer = middle_pointer + 1

            else:
                right_pointer = middle_pointer - 1

        return left_pointer


# 1, 3, 5, 6, target = 7
nums = [1, 3, 5, 6]
target = 2

sol = Solution()
result = sol.searchInsert(nums, target)
print(result)
