from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left_pointer = 1

        for right_pointer in range(1, len(nums)):
            if nums[right_pointer] == nums[left_pointer - 1]:
                continue
            else:
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1

        return left_pointer
