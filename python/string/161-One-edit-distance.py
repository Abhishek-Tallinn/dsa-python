# Problem: Leetcode 161 - One Edit Distance
# Difficulty: Medium
# Link: https://leetcode.com/problems/one-edit-distance/description/
# Time Complexity: O(n) as we iterate through one string
# Space Complexity: O(n) as new immutable strings are created.
# Approach: We ensure that s is smaller than t by switching them is s is longer. then we run a loop on s and check it with t. if a mismatch is found
# then we see the lengths. If s and t have equal lengths then then remaining characters in both should be equal as we can replace the mismatch. but if 
# t is longer than s then we check s[i:] to t[i+1:] and if they are equal then equality can be achieved by inserting character in s.
# at the end it possible that no mismatch was found. so we check that if length of t is only 1 greater than s then we can make them equal by one insertion.
# else we return False

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s,t = t,s
        if abs(len(t) - len(s))>1:
            return False
        ls , lt = len(s), len(t)
        for i in range(ls):
            if s[i]!=t[i]:#diff spotted
                # then we compare the rest of the string
                if ls<lt:
                    return s[i:] == t[i+1:] # we can make them equal by inserting
                else:
                    return s[i+1:] == t[i+1:]
                
        if (lt - ls) ==1:
            return True
        
        return False