# Problem: Leetcode 482 - License key formatting
# Difficulty: Easy
# Link: https://leetcode.com/problems/license-key-formatting/description/
# Time Complexity: O(n) - where n is the length of the input address
# Space Complexity: O(n) as we add items to answer array
# Approach: We count the number of group and hence the number of items that will enter in the first group. If a first group will exist we add characters to it and add a '-'. then from second group onwards we iterate
# over the remaining string and collect k items and keep adding '-' after k items.


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cnt = 0
        for char in s:
            if char!="-":
                cnt+=1
        groups = cnt//k
        first_group_length = cnt - groups*k
        ans = []
        i=0
        if first_group_length>0:
            while first_group_length>0:
                if s[i] == "-":
                    i+=1
                    continue
                ans.append(s[i].upper())
                i+=1
                first_group_length-=1
            ans.append('-')
        counter = 0
        for j in range(i,len(s)):
            if s[j]=='-':
                continue
            ans.append(s[j].upper())
            counter+=1
            if counter==k:
                ans.append('-')
                counter = 0
        if ans:
            ans.pop()
        return ''.join(ans)
            