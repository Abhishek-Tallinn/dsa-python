# Problem: Leetcode 3871 - Count commas in range II
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-commas-in-range-II/description/
# Time Complexity: O(k) where k is the number of digits as we reduce one digit at a time
# Space Complexity: O(1)
# Approach: We take the initial commas by subtracting the just smaller power of 10 from the number and producing a mask
# and then we keep dividing mask by 10 in a while loop and for each value of mask we keep taking the commas
# that would be in that total range of numbers. This we do with our helper function. Then we keep adding the commas
# and we return the total value.


class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        if n < 1000:
            return 0
        def comma_nos(n):
            if len(str(n))>=16:
                return 5
            elif len(str(n))>=13:
                return 4
            elif len(str(n))>=10:
                return 3  
            elif len(str(n))>=7:
                return 2
            elif len(str(n))>=4:
                return 1
            else:
                return 0
        
        no_of_digits = len(str(n))
        mask = 10**(no_of_digits-1)
        #initialize the starting commas
        total_commas += int((n - mask+1)*comma_nos(n))
        while mask>=1000:
            total_commas+=int(comma_nos(mask//10)*(mask-mask//10))
            mask = mask//10
        return total_commas