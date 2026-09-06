# Problem: Leetcode 763 - Partition labels
# Difficulty: Medium
# Link: https://leetcode.com/problems/partition-labels/description/
# Time Complexity: O(n)
# Space Complexity: O(1) - although we use space to store answer array
# Approach: We make a hashmap tracking the last_idx of each character. As we iterate over the string, we keep 
# calculating the mx_break_idx based on which character we saw before we reach the break index can extend this boundary. We need to remember
# that idea is to brings string into maximum parts so we are trying to break at the earliest. 
# If index reach the mx_break_index meaning no other character seen till now occurs beyond this index and we can break the string here
# so we append length of this part to answer and reset our start pointer and reset mx_break_index to 0
# we return ans at the end

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {char:idx for idx,char in enumerate(s)}
        ans = []
        mx_break_idx = 0
        start = 0
        for i in range(len(s)):
            mx_break_idx = max(mx_break_idx,last_idx[s[i]])
            if i == mx_break_idx:
                ans.append(i-start+1)
                start = i+1
                mx_break_idx = 0
        return ans