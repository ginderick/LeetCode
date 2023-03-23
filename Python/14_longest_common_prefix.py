from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Return empty string if list is empty
        if not strs:
            return ""

        # Set the first index of the list as the initial shortest word
        shortest_word = strs[0]

        # Determine the shortest word
        for index in range(1, len(strs)):
            word = strs[index]
            if len(shortest_word) > len(word):
                shortest_word = word

        # Iterate all the words if they have common prefix
        for index, value in enumerate(shortest_word):

            for word in strs:
                if word[index] != value:
                    return shortest_word[:index]
        return shortest_word
