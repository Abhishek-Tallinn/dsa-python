# Problem: Leetcode 2129 - Capitalize the title
# Difficulty: Easy
# Link: https://leetcode.com/problems/capitalize-the-title/description/
# Time Complexity: O(n) - passing over each character of string
# Space Complexity: O(k) where k is the number of words in title that are sliced
# Approach: We split the string and then iterate over the words.If length of word is 1 or 2 we just append the lower form of it and if it is
# more than 2 we first make it lowercase and then capitalize the first letter and append it.


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        t = title.split(' ')
        res = []
        for word in t:
            if len(word)==1 or len(word)==2:
                lower_word = word.lower()
                res.append(lower_word)
            else:
                l_word = word.lower()
                camel_word = l_word[0].upper() + l_word[1:]
                res.append(camel_word)

        return ' '.join(res)