# Problem: Leetcode 2033 - Mininmum Operations to Make a Uni-Value Grid 
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Approach: Since we have to minimize operations, we can use the median of the list as the target value. We can calculate the total operations needed to convert all elements to the median. If any element cannot be converted to the median (i.e., if the difference is not a multiple of x), we return -1.


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m,n = len(grid), len(grid[0])
        #handle base case
        if m == 1 and n == 1:
            return 0
        #flatten the list to make access easier
        nums= []
        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j]) 
        median = nums[len(nums)//2]
        total_ops = 0
        for num in nums:
            if num!=median and (num-median)%x !=0:
                return -1
            total_ops+=abs(num-median)//x
        return total_ops
