# Problem: Leetcode 3517 - Smallest palindromic rearragement I
# Difficulty: Medium
# Link: https://leetcode.com/problems/smallest-palindromic-rearragement-i/description/
# Time Complexity: O(n log n) as we effectively make one pass over array
# Space Complexity: O(n) as we make a hashmap
# Approach: We collect the characters, sort them and then place them one by one at the front and back in the sequence to make the 
# lexicographically smallest palindrome possible. We just need to keep into account the special case 
# where there is a character with odd value so then we keep one count of this character in the center as this is the one which makes 
# the overall length of palindrome odd and then we continue as usual placing our characters at front and back in sequence.
# then we return our answer.

from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1 or len(set(s))==1:
            return s
        d = Counter(s)
        s_d = dict(sorted(d.items(),key = lambda x:x[0]))
        ans = ['0']*len(s)
        k = 0
        for key,val in s_d.items():
            if val%2==1:
                ans[len(s)//2] = key
                val = val-1
            while k< len(ans) and val>0:
                ans[k] = key
                ans[len(s)-k-1] = key
                val-=2
                k+=1

        return ''.join(ans)