# Problem: Leetcode 500 - Keyboard row
# Difficulty: Easy
# Link: https://leetcode.com/problems/keyboard-row/description/
# Time Complexity: O(n) as we check words array
# Space Complexity: O(1) as three sets only have total of 26 alphabets
# Approach: We simply create three sets of each keyboard row for fast look up.
# then for each word we check that if it can be typed with only one row(one set that means) and if yes then we keep appending it to our result.
# then we return result. We can also possibly check it this way that if a word <= set meaning that a word is a subset of set then we can append it to result.

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        res = []
        for word in words:
            lword = word.lower()
            if all(char in first for char in lword) or all(char in second for char in lword) or all(char in third for char in lword):
                res.append(word)
        return res