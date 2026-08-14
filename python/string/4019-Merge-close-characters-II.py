# Problem: Leetcode 4019 - Merge close characters II
# Difficulty: Medium
# Link: https://leetcode.com/problems/merge-close-characters-ii/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach - we record the last seen position of each character in the hashmap and keep looking at each character and check if its current position is whithin
# k range of the previous seen index. If yes then we skip else we update the last position and add it to result

class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        last_pos= {}
        result = []
        for c in s:
            if c in last_pos and len(result)-last_pos[c]<=k:
                continue
            last_pos[c] = len(result)
            result.append(c)
        return "".join(result)