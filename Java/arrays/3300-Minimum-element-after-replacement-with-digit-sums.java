/* 
# Problem: Leetcode 3300 - Minimum element after replacement with digit sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/
# Time Complexity: O(n.k) where k is the length of each number but reduces to O(n)
# Space Complexity: O(1) as no extra space used
# Approach: We simply loop over the array and add the calculate sum of digits and keep a min ans variable which we keep updating 
*/


import java.util.*;

class Solution {
    public int minElement(int[] nums) {
        int mn = Integer.MAX_VALUE;
        for(int num: nums){
            int s = 0;
            while (num>0){
                int d = num%10;
                s+=d;
                num = num/10;
            }

            mn = Math.min(mn,s);
            }
        return mn;
    }
}