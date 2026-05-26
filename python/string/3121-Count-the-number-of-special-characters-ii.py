# Problem: Leetcode 3121 - Count the Number of Special Characters II
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/
# Time Complexity: O(n) as we loop through string to make a hashmap and then one more loop to count so O(n) + O(n) = O(n)
# Space Complexity: O(n) as we use two hashmaps which can be of length n
# Approach: We iterate over the string the find the index of first uppercase and the last lowercase character for each character. 
# Then we loop through lowercase letters hashmap and check if its in the uppercas hashmap and if the index is lower than uppercase and then we increment the counter and return it.
# Approach2: There is another approach below where we first use hashmap to find first occurence only of the uppercase character.
# Then we loop backwards on original string and if a lowercase character is found(which would be its last occurrence ofcours) we check if the index is less than its uppercase index in uppercase hashmap.
# If yes then we increment count and we also add this to the seen set to avoid counting duplicate values.


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = {}
        last_lower = {}

        for i, ch in enumerate(word):
            if ch.isupper() and ch not in first_upper:
                first_upper[ch] = i
            if ch.islower():
                last_lower[ch] = i # i keep overwriting the values to track the last one

        cnt = 0
        for ch in last_lower:
            if ch.upper() in first_upper and last_lower[ch] < first_upper[ch.upper()]:
                cnt += 1

        return cnt
        '''
        index_map = {}
        for idx,char in enumerate(word):
            if char.isupper() and char not in index_map:
                index_map[char] = idx
        #every lowercase occurrence so no set conversion.
        cnt = 0
        seen=set()
        for i in range(len(word)-1,-1,-1):
            if word[i].islower() and word[i] not in seen and word[i].upper() in index_map:
                if i < index_map[word[i].upper()]:
                    cnt+=1
            seen.add(word[i])
        return cnt
        '''
       
        