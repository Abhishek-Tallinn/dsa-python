# Problem: Leetcode 3083- Existence of a substring in a string and its reverse
# Difficulty: Easy
# Link: https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we make a set
# Approach1: we add pairs to a set and then we iterate again to see it reverse of any pair is also in seen and if it is we return true
# Approach2: we reverse the string first so we dont reverse it in loop and then we make only one loop and check
# if the substr is in the reverse and if yes we return true. This takes only one loop but goes to O(n^2).

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        seen = set()
        for i in range(len(s)-1):
            seen.add(s[i:i+2])
        for sub in seen:
            if sub[::-1] in seen:
                return True
        return False
        '''
        compute reverse one but not in loop as it casues O(n^2)
        rev = s[::-1]
        for i in range(len(s)-1):
            substr = s[i:i+2]
            if substr in rev:
                return True
        return False 
        '''
        