from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        number_dict = {}

        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in number_dict:
                return [number_dict[remainder], index]
            number_dict[value] = index

        return number_dict
