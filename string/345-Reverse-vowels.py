# Problem: Leetcode 345 - Reverse Vowels of a string
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Quite straightforward approach to use two pointers after writing the string in a list and then use two pointers from two ends
# to switch when vowels are found


class Solution:
    def reverseVowels(self, s: str) -> str:

        left = 0
        right = len(s)-1
        vowels = set('aeiouAEIOU')
        res = [char for char in s]
        while left<right:
            if res[left] not in vowels:
                left+=1
            elif res[right] not in vowels:
                right-=1
            else:
                res[left],res[right] = res[right],res[left]
                left+=1
                right-=1
        return ''.join(res)