/*
Problem: Leetcode 1 - Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/description/
# Time Complexity: O(n) where n is the size of the matrix.
# Space Complexity: O(n) as we use a map
# Approach: we keep adding elements to hashmap and before every addition we check if its complement exists in the map. 
# if it does then we can just return the index of the complement and the current index which is our answer
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map()
    for(let i = 0;i<nums.length;i++){
        if (map.has(target-nums[i])){
            return [map.get(target-nums[i]),i]
        }
        map.set(nums[i],i)
    }
};