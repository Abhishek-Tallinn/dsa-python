# Problem: Leetcode 2937 - Make three strings equal
# Difficulty: Easy
# Link: https://leetcode.com/problems/make-three-strings-equal/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we make and iterate over list of strings
# Approach1: We iterate over the shortest of the three string and if character at the index in all three index are not equal we break after seeting target at that index.
# then we iterate over each string and count the number of character to drop to make the length equal to target
# Appraoch2: More pythonic. We see that problem is basically asking longest common prefix. We iterate over the string and we calculate the longest prefix.
# then we iterate over each string and cumulatively count the difference between each string length and the longest prefix as that is the amount of characters we have to drop from each string.
# then we return count

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        target = 0
        for i in range(0,min(n1,n2,n3)):
            if (s1[i]!=s2[i] or s2[i]!=s3[i] or s1[i]!=s3[i]):
                target = i
                break
            else:
                target+=1
        if target == 0:
            return -1
        
        cnt = 0
        strs = [s1,s2,s3]
        for s in strs:
            cnt += len(s)-target
        return cnt
        
        '''
        def longest_common_prefix(strs):
            if not strs:
                return ""
            prefix = []
            for chars in zip(*strs):
                if len(set(chars))==1:
                    prefix.append(chars[0])
                else:
                    break
            return ''.join(prefix)

        strs = [s1,s2,s3]
        cnt = 0
        p = longest_common_prefix(strs)
        if not p:
            return -1
        for s in strs:
            cnt += len(s)-len(p)
        return cnt
        '''