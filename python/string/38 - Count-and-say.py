# Problem: Leetcode 38 - Count and Say
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-and-say/description/
# Time Complexity: O(2^n) as time will grow exponentially as we are generating the string for n-1 and iterating through it.
# Space Complexity: O(2^n) as string length will grow exponentially too so total space will be proportional to the final string size.
# Approach: set up a base case of "1" and set up a while loop to go through all n cases.
# At each iteration, generate the new string by iterating through the previous string and counting the number of times a digit is repeated and then adding that count and the digit to the new string. 
# Then make this new string as the new base case. 
# Finally return the base case which will be updated to the final string after n iterations.


class Solution:
    def countAndSay(self, n: int) -> str:
        
        base = "1"
        i = 1
        while i < n:
            new = ""
            right = 0
            while right < len(base):
                repeat_count = 1
                
                while right+1 < len(base) and base[right] == base[right+1]:
                    repeat_count+=1
                    right+=1
                new += str(repeat_count)+base[right]   
                right+=1
                       
            base = new
            i+=1
                
        return base
