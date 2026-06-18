# Problem: Leetcode 819 - Most common word
# Difficulty: Easy
# Link: https://leetcode.com/problems/most-common-word/description/
# Time Complexity: O(n) as we iterate over string
# Space Complexity: O(n) as we make a final list of words for dictionary and O(n) for counter map also
# Approach: We clean the string with re library and split it into words. then we remove any empty string and make counter hashmap.
# then we iterate in hashmap and find the word with max freq which is not in banned. banned we convert to a set for O(1) look up

import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        banned = set(banned)
        words = re.split(r'[!?\',;. ]+',paragraph)
        final = [w for w in words if w!='']
        d = Counter(final)
        mx_f = 0
        ans = ""
        for word,freq in d.items():
            if word not in banned:
                if freq>mx_f:
                    mx_f = freq
                    ans = word

        return ans