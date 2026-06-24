# Problem: Leetcode 3280 - Convert data to binary
# Difficulty: Easy
# Link: https://leetcode.com/problems/convert-date-to-binary/description/
# Time Complexity: O(n) for split operations
# Space Complexity: O(n) for ans array
# Approach: We split the date string across '-' and convert each integer value to binary and append it back to ans array to be returned as a string.
# Since we append '-' after every value conversion there is a '-' at the end so we also do ans.pop() to remove the last '-' before returning

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        nums = date.split('-')
        ans = []
        for num in nums:
            ans.append(bin(int(num))[2:])
            ans.append('-')
        ans.pop()
        return ''.join(ans)