# Problem: Leetcode 42 - Trapping Rain Water
# Difficulty: Hard
# Link: https://leetcode.com/problems/trapping-rain-water/description/
# Time Complexity: O(n) as we iterate through the array elements
# Space Complexity: O(n) as we use a stack to push and pop elements
# Approach: Use a stack to keep track of indices of array elements in increasing order of their heights. For each element, calculate the trapped water with the element as the smallest one and update the total trapped water.
# We have stack based approach and also the precomputed approach where we precompute the left max and right max for each element and then calculate the water level and add to total trapped water.


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        #stack appraoch
        stack = []
        trapped = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                base = stack.pop()
                if stack:
                    left_wall = stack[-1]
                    width = i - stack[-1] -1
                    h = min(height[i],height[left_wall]) - height[base]
                    trapped+=width*h
            stack.append(i)
        return trapped


        ''' 
        this is precomputed appraoch. we can do with two pointers or stack
        n = len(height)
        left_max = [0]*n
        right_max= [0]*n

        left_max[0] = height[0]
        right_max[n-1] = height[n-1]

        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i])
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])
        total = 0
        for i in range(n):
            water_level = min(left_max[i],right_max[i])
            total += water_level - height[i]
        return total
        '''