from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        right_max = -1

        for i in range(len(arr) - 1, -1, -1):
            new_max = max(arr[i], right_max)
            arr[i] = right_max
            right_max = new_max
        return arr


sol = Solution()
input = [17, 18, 5, 4, 6, 1]
result = sol.replaceElements(input)
print(result)
