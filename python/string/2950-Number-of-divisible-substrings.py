# Problem: Leetcode 2950 - Number of divisible substrings
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-divisible-substrings/description/
# Time Complexity: O(n^2) as we need to check each substring
# Space Complexity: O(n) as we we need to make prefix array
# Approach: We make a prefix array for O(1) query for each substring. The prefix array is based on a map of alphabets 
# with their respective values. then we generate all substrings with a nested loop and do quick prefix query to check if their 
# value is divisible by their length and increment our counter. we return counter at the end

class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        mapping = {
            'a': 1,'b':1,'c':2,'d':2,'e':2,'f':3,'g':3,'h':3, 
            'i':4,'j':4,'k':4,'l':5,'m':5,'n':5,'o':6,'p':6,'q':6,
            'r':7,'s':7,'t':7,'u':8,'v':8,'w':8,'x':9,'y':9,'z':9
        } 
        prefix = [0] * (len(word) + 1)
        for i in range(len(word)):
            prefix[i+1] = prefix[i] + mapping[word[i]]
        cnt = 0
        for i in range(len(word)):
            for j in range(i,len(word)):
                if (prefix[j+1] - prefix[i]) % (j-i+1) == 0:
                    cnt+=1    
        return cnt