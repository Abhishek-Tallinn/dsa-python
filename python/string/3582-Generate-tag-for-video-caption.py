# Problem: Leetcode 3582 - Generate tag for video caption
# Difficulty: Easy
# Link: https://leetcode.com/problems/generate-tag-for-video-caption/description/
# Time Complexity: O(n) which is use by split in built function
# Space Complexity: O(n) as we store words array
# Approach: After creating words array with split if its not empty we convert each word to titlecase with in built title() function by list comprehension.
# we have to avoid common mistake of for word in words as word becomes a refrence to element in words and does not actually change it.
# then we just separately make the first words of words as lowercase and append a # and return the answer string.

class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words:
            return '#'
        words = [word.title() for word in words]
        #for word in words:
        #    word = word.capitalize()
        words[0] = words[0].lower()
        ans = ''.join(words)
        final = '#'+ans
        return final[:100] 