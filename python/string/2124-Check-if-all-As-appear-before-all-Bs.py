# Problem: Leetcode 2124 - Check if all As appear before all Bs
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-all-As-appear-before-all-Bs/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use hashmap
# Approach: We make a hashmap where we map the last index of A. then we iterate over the string and the moment we find 'b'
# we just return if current b index > the last as index found. the exception is that if there is no A or no B in the string
# then we return true invariably.

class Solution:
    def checkString(self, s: str) -> bool:
        last_a = {char:idx for idx,char in enumerate(s) if char=='a'}
        if not last_a:
            return True
        for i,ch in enumerate(s):
            if ch=='b':
                return i>last_a['a']
        return True