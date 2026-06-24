# Problem: Leetcode 3210 - Find the encrypted string
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-encrypted-string/description/
# Time Complexity: O(n) - passing over each character of string
# Space Complexity: O(n) as we create the answer
# Approach: We convert the string to a list and then iterate over it replace each character in a cycling manner and then return the ans string.

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        l = [char for char in s]
        ans = ['']*len(l)
        for i in range(len(l)):
            ans[i] = l[(i+k)%len(l)]
        return ''.join(ans)