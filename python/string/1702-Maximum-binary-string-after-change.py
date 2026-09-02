# Problem: Leetcode 1702 - Maximum Binary String After Change
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-binary-string-after-change/description/
# Time Complexity: O(n) - as we iterate through the string
# Space Complexity: O(n) as we build the result string
# Approach: The solution is based on greedy observation that all 1s can be bubbled up to the end
# and then all ones on left are left as it is and the zeros in between or the beginning(if there are no 1's on the left) are converted to 10 so 
# only one zero will be left out of all the zeros. Based on this observation we just construct our answer string.
# the answer will be all starting 1s in their place, then all 1s which are just converted zeros but the last one will be 0 and then all ones which were not at the beginning are appended to the end
# this will be the biggest string we can make.

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        ans = []
        ones = binary.count('1')
        zeros = len(binary) - ones
        if not zeros:
            return binary
        left = 0
        while left<len(binary) and binary[left]=='1':
            ans.append(binary[left])
            ones-=1
            left+=1
        if left==len(binary):
            return ''.join(ans)
        for i in range(zeros):
            if i == zeros-1:
                ans.append('0')
            else:
                ans.append('1')
        for _ in range(ones):
            ans.append('1')
        #usually construction is in one way with a string thing or an array thing
        return ''.join(ans)
