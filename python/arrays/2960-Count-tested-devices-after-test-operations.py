#Problem: Leetcode 2960 - Count tested devices after test operations
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-tested-devices-after-test-operations/description/
# Time Complexity: O(n) as we loop on batteryPercentages
# Space Complexity: O(1) as we only use pointers
# Approach: We keep a decrement counter which increases everytime we are able to decrement a battery by one and each subsequent battery
# is checked against this decrement counter. If after subtracting decrement counter its still >0 then we know 
# that this battery will survive and we can increment our counter.

from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        dec=0
        cnt=0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i]-dec >0:
                cnt+=1
                dec+=1
        return cnt