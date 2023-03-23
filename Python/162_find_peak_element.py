from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        highest_index = 0
        for i in range(1, len(nums)):
            if nums[highest_index] < nums[i]:
                highest_index = i
            continue
        return highest_index
