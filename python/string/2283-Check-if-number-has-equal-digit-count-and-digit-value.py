# Problem: Leetcode 2283 - Check if number has equal digit count and digit value
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use a hashmap 
# Approach: We make hashmap of num and then compare each index value with its freq in the map as per the condition in question.
# if any index fails we return False

from collections import Counter
class Solution:
    def digitCount(self, num: str) -> bool:
        freq = Counter(num)
        return all(int(num[i]) == freq[str(i)] for i in range(len(num)))