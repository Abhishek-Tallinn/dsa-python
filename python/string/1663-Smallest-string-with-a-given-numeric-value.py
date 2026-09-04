# Problem: Leetcode 1663 - Smallest string with a given numeric value
# Difficulty: Medium
# Link: https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/description/
# Time Complexity: O(n) as we perform join operations
# Space Complexity: O(n) as we make a string
# Approach: We simply check at each index if we can put an 'a' to keep it lexicographically minimum 
# If not then we put the smallest character in range which will allow us to reach the total of K by placing all z's on the 
# remaining indices

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ['']*n
        for i in range(n):
            if (n-1-i) * 26 >= k:
                ans[i] = 'a'
                k-=1
            else:
                ans[i] = chr((k - (n-i-1)*26) + 96)
                k-=(ord(ans[i]) - ord('a')+1)

        return ''.join(ans)