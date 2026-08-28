/* 
# Problem: Leetcode 2960 - Count tested devices after test operations
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-tested-devices-after-test-operations/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We keep a decrement counter which increases everytime we are able to decrement a battery by one and each subsequent battery
# is checked against this decrement counter. If after subtracting decrement counter its still >0 then we know 
# that this battery will survive and we can increment our counter.
*/

class Solution {
    public int countTestedDevices(int[] batteryPercentages) {
        int cnt=0,dec = 0;
        for (int i=0;i<batteryPercentages.length;i++){
            if(batteryPercentages[i]-dec>0) {cnt++; dec++;}
        }
        return cnt;
    }
}