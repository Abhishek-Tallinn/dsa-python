# Problem: Leetcode 3412 - Find mirror score of a string
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-mirror-score-of-a-string/description/
# Time Complexity: O(n) as we go through the hashmap
# Space Complexity: O(n) as we use the dictionary 
# Approach: We make a hashmap where we store the indexes of the characters that we have seen previously. 
# and for current character if the mirror is in hashmap and all indexes are not popped then we calculate the score and move forward 
# without adding the current element in the hashmap. So its hashmap based stack.

from collections import defaultdict
class Solution:
    def calculateScore(self, s: str) -> int:
        
        d = defaultdict(list)
        score = 0
        for i,char in enumerate(s):
            mirror = chr(ord('z')- (ord(char)-ord('a')))
            if d[mirror]:
                score+=i-d[mirror].pop()
            else:
                d[char].append(i)
        return score
        

        '''
        usual stack - TLE
        for i in range(len(s)):
            temp = []
            d[s[i]] = i
            if mirror(s[i]) not in d:
                stack.append(i)
                continue
            while stack and s[stack[-1]]!=mirror(s[i]):
                temp.append(stack.pop())
            
            if stack:
                score+= i - stack[-1]
                stack.pop() #unmark the mirror element
                if temp:
                    stack.extend(temp[::-1])
                continue
            if temp:
                stack.extend(temp[::-1])
            stack.append(i)
        return score
        '''
    