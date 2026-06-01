# Problem: Leetcode 1243 - Array Transformation
# Difficulty: Medium
# Link: https://leetcode.com/problems/array-transformation/description/
# Time Complexity: O(n * k) where n is the length of the array and k is the number of iterations needed.
# Space Complexity: O(n) for storing the transformed array.
# Approach: Simulate the transformation process by iterating through the array and updating each element based on its neighbors. Continue until no more changes occur.
# We need to create a copy of the array and create a totally new array based on that copy and then compare both at end of the loop to reach the break condition.
# In place modification is not required by this question


from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        curr_day = arr[:]
        while True:
            new_day = [curr_day[0]]
            for i in range(1,len(arr)-1):
                if curr_day[i]<curr_day[i-1] and curr_day[i] < curr_day[i+1]:
                    new_day.append(curr_day[i]+1)
                elif curr_day[i] > curr_day[i-1] and curr_day[i] > curr_day[i+1]:
                    new_day.append(curr_day[i]-1)
                else:
                    new_day.append(curr_day[i])
            new_day.append(curr_day[-1])
            if new_day == curr_day:
                break
            curr_day = new_day[:] # dont need copy here as we are rebuilding new_day which is safe 
            # mutating new day wont be safe as curr_day would also change
            
        return new_day