# Problem: Leetcode 3240 - Check balanced string
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-balanced-string/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We just calculate sum of digits on even and odd positions and return True if they are equal


class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = odd_sum =0
        for i in range(0,len(num)):
            if i%2==0:
                even_sum+=int(num[i])
            else:
                odd_sum+=int(num[i])
       
        return odd_sum == even_sum