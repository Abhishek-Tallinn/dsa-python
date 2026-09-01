# Problem: Leetcode 1859 - Sorting the Sentence
# Difficulty: Easy
# Link: https://leetcode.com/problems/sorting-the-sentence/description/
# Time Complexity: O(n) - as we iterate through the string
# Space Complexity: O(n) - as we store the words in a dictionary
# Approach: We split the sentence into words, extract the position from each word, and place the word in the correct position in the result array.
# The words based index are stored in hashmap and then we iterate over each answer index and get the value for the hashmap for each index of ans.
# then we  just join ans and return it as a string

class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        words = s.split(" ")
        for word in words:
            d[word[-1]] = word[:len(word)-1]
        ans = [""]*len(words)
        for i in range(len(ans)):
            ans[i] = d[str(i+1)]
        return ' '.join(ans) 