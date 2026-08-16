# Problem: Leetcode 804 - Unique morse code words
# Difficulty: Easy
# Link: https://leetcode.com/problems/unique-morse-code-words/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a set
# Approach: we transform each word and store in set. Then we just return the length of the set

from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        cnt = 0
        for word in words:
            transformed = []
            for char in word:
                transformed.append(morse_code[ord(char)-ord('a')])
            if "".join(transformed) in s:
                continue
            s.add("".join(transformed))
            cnt+=1
        return cnt