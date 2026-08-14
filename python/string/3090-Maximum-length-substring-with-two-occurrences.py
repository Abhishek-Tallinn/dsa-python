# Problem: Leetcode 3090- Maximum length substring with two occurrences
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We use a sliding window and use a hashmap to keep frequency at each character at every iteration. 
# if the freq of the new character on the right is within the limit of 2. If it is then we update our max else we make the window valid again.


from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d = defaultdict(int)
        left = 0
        mx = 0
        for right in range(len(s)):
            d[s[right]]+=1
            while left<right and d[s[right]]>2:
                d[s[left]]-=1
                left+=1
            
            mx = max(mx,right-left+1)
        return mx