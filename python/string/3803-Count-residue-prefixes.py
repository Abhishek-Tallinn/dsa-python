# Problem: Leetcode 3803 - Count residue prefixes
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-residue-prefixes/description/
# Time Complexity: O(n)
# Space Complexity: O(k) where k is the size of set
# Approach2- original: I iterate on string and keep a set to track distinct characters. If char is duplicate i increment only prefix length and if its distinct i increment both lengths.
# then at each iteration i check if distinct length == prefix length%3
# Approach1(more optimized) - We can do more efficient check where prefix length is tracked by index of iteration and we just keep adding distinct character to set. 
# and other each iteration we check if length of set == index%3 and if yes we increment our counter

class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        ans = 0
        for idx,char in enumerate(s,1):
            if char not in seen:
                seen.add(char)
            if len(seen) == idx%3:
                ans+=1
        return ans
        '''
        p_len = 0
        d_cnt = 0
        ans = 0
        for char in s:
            if char in seen:
                p_len+=1
            else:
                d_cnt+=1
                p_len+=1
                seen.add(char)
            if d_cnt == p_len%3:
                ans+=1
        return ans
        '''