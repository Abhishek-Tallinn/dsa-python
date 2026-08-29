# Problem: Leetcode 2269 - Find the k beauty of a number
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/
# Time Complexity: O(n) 
# Space Complexity: O(1) 
# Approach: We simply take each substring of length k and check if it divides nums and increment out counter
# we skip if n is 0 to avoid division by 0 error


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        cnt = 0
        s = str(num)
        for i in range(len(s)-k+1):
            n = int(s[i:i+k])
            if n==0:
                continue
            if num%n==0:
                cnt+=1
        return cnt 