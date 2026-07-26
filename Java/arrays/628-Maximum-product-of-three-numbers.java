/* 
# Problem: Leetcode 628 - Maximum product of three numbers
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-product-of-three-numbers/description/
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Approach: The key insight is that once your sort the maximum sum can be produced either by the 
# three biggest numbers or two smallest negative ones(for +ve sign) and the largest positive one. we return 
# max of both those values.
*/
import java.util.*;
class Solution {
    public int maximumProduct(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        return Math.max(nums[n-1]*nums[n-2]*nums[n-3], nums[0]*nums[1]*nums[n-1]);
        
    }
}