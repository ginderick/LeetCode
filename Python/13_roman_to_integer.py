class Solution:
    def romanToInt(self, s: str) -> int:

        roman_numerals_dict = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }

        number = 0

        s = (
            s.replace("IV", "IIII")
            .replace("IX", "VIIII")
            .replace("XL", "XXXX")
            .replace("XC", "LXXXX")
            .replace("CD", "CCCC")
            .replace("CM", "DCCCC")
        )

        for char in s:
            number += roman_numerals_dict[char]

        return number


class Solution_2:
    def romanToInt(self, s: str) -> int:
        roman_numerals_dict = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }

        number = 0

        for index in range(0, len(s) - 1):

            if roman_numerals_dict[s[index]] < roman_numerals_dict[s[index + 1]]:
                number -= roman_numerals_dict[s[index]]
            else:
                number += roman_numerals_dict[s[index]]

        return number + roman_numerals_dict[s[-1]]
