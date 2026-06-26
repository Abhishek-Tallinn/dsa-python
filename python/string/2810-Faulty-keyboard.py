# Problem: Leetcode 2810 - Faulty keyboard
# Difficulty: Easy
# Link: https://leetcode.com/problems/faulty-keyboard/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use a deque
# Approach1: We use a straightforward approach where we iterate over the string and reverse it everytime we see an i but this cost additional O(n) time to reverse the string
# Approach2: We use a deque where everytime we see i we toggle the reverse flag. During iteration if reverse flag is true we append to the left in queue and if its false we append usually to the right.
# after loop ends we check once more if the flag is true to reverse the string. then we return the string after joining it.

from collections import deque

class Solution:
    def finalString(self, s: str) -> str:
        ans = deque()
        r_flag = False
        for char in s:
            if char == 'i':
                r_flag = not r_flag
            else:
                if r_flag:
                    ans.appendleft(char)
                else:
                    ans.append(char)
        if r_flag:
            ans.reverse()
        
        return ''.join(ans)
        '''
        ans = []
        for char in s:
            if char=='i':
                ans = ans[::-1]
            else:
                ans.append(char)
        return ''.join(ans)
        '''