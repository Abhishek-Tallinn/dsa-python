# Problem: Leetcode 12 - Integer to Roman
# Difficulty: Medium
# Link: https://leetcode.com/problems/integer-to-roman/description/
# Time Complexity: O(1) as we just have a hasmap of 13 fixed values
# Space Complexity: O(1) as we break down the number and now new space is used
# Approach: In a for loop just keep calculating the quotient and remainder for each value of hashmap and keep appending the correct roman numerals to the roman list.
# Then we can return the list.


class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman_digits = []
        # Loop through each symbol.
        for value, symbol in digits:
            # We don't want to continue looping if we're done.
            if num == 0:
                break
            count, num = divmod(num, value)
            # Append "count" copies of "symbol" to roman_digits.
            roman_digits.append(symbol * count)
        return "".join(roman_digits)
        
       
    
        return answer