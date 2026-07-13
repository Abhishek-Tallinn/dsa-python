# Problem: Leetcode 1291 - Sequential digits
# Difficulty: Medium
# Link: https://leetcode.com/problems/sequential-digits/description/
# Time Complexity: O(1) - only 36 numbers
# Space Complexity: O(1) - only 36 numbers so constant space
# Approach: Quite simple once you realize only 36 possible number are possible in the answer.
# So you make a sequence list and then iterate over it collecting only those values which are between low and high


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        sequence = [12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]
        ans = [num for num in sequence if num>=low and num<=high]
        return ans