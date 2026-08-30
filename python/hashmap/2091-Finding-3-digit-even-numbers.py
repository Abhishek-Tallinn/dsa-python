# Problem: Leetcode 2091 - Finding 3 digit even numbers
# Difficulty: Easy
# Link: https://leetcode.com/problems/finding-3-digit-even-numbers/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use a counter hashmap
# Approach: We go through all the 3 digit even numbers and check if its possible to make it with the digits array
# by comparing the freq of each digit in hashmap of digits. If we have enough freq of each digit then we append it to answer.

from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        s = Counter(digits)
        ans = []
        for i in range(100,1000,2):
            possible = True
            t = Counter(str(i))
            for key,value in t.items():
                if int(key) not in s or value > s[int(key)]:
                    possible = False
                    break
            if possible:
                ans.append(i)
        return ans