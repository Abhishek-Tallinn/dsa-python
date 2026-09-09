# Problem: Leetcode 3870 - Count commas in range 
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-commas-in-range/description/
# Time Complexity: O(k) where k is the number of digits as we reduce one digit at a time
# Space Complexity: O(1)
# Approach: We take the initial number of commas between the number and the closest smaller power of 10.
# then we start reducing the mask with power of 10 and for each range of mask-mask//10 which will cover all numbers in one power of 10 range then
# we just multiple this range with how many commas each number in range will have and update the total commas
class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        if n < 1000:
            return 0
        
        mask = 10**(len(str(n))-1)
        total_commas += (n - mask+1) #initial
        while mask>1000:
            total_commas+=1 * (mask-mask//10)
            mask = mask//10
        return total_commas
        #how to do manually
        #elif 1000<=n <= 9999:
        #    return (n-1000+1)
        #else:
        #    return 9000+(n-10000+1)