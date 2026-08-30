# Problem: Leetcode 2103 - Rings and rods
# Difficulty: Easy
# Link: https://leetcode.com/problems/rings-and-rods/description/
# Time Complexity: O(n) as we loop rings once and then memo once
# Space Complexity: O(n) as we use memo hashmap
# Approach: We iterate rings and take color and rod of each ring and add it to hashmap with rod being the key
# and each key will hold all the color rings it has. Then we iterate over memo hashmap and check which key has
# 3 unique colors. Its a common pitfall to generally check for key having a list of length 3 as value and counting it 
# but that is wrong as colors could repeat. We count only when 3 unique values exist.


from collections import defaultdict
class Solution:
    def countPoints(self, rings: str) -> int:
        memo = defaultdict(list)
        for i in range(0,len(rings),2):
            current_color = rings[i]
            current_rod = rings[i+1]
            memo[current_rod].append(current_color)
        cnt = 0
        for ring,colors in memo.items():
            if len(set(colors))==3:
                cnt+=1
        return cnt 