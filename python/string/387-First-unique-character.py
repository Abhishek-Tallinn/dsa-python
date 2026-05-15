# Problem: Leetcode 387 - First unique character in a string
# Difficulty: Easy
# Link: https://leetcode.com/problems/first-unique-character-in-a-string/description/
# Time Complexity: O(n) - passing over each character of string
# Space Complexity: O(1) - saving only 26 letters
# Approach: We make a frequency hash map and then we iterate over the original string and if the freq matches we return the index
# Approach2 is more efficient in a streaming sense that it does it in one pass by maintaining a queue.
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = Counter(s)

        for idx,char in enumerate(s):
            if char_map[char] == 1:
                return idx
        return -1
        
        '''
        In single pass in streaming system
        freq = Counter()
        q = deque()

        for i, ch in enumerate(s):
            freq[ch] += 1
            q.append((ch, i))

            # remove invalid front
            while q and freq[q[0][0]] > 1:
                q.popleft()

        return q[0][1] if q else -1
        '''