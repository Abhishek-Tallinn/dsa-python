# Problem: Leetcode 1678 - Goal parser interpretation
# Difficulty: Easy
# Link: https://leetcode.com/problems/goal-parser-interpretation/description/
# Time Complexity: O(n) as we perform join operations
# Space Complexity: O(1)
# Approach: We simply iterate over the string and append to ans array based on instructions. If we find g,
# we append "G" and if we find brackets if append "o" and jump 2 indices and if we find '(al)' then we append 'al' and 
# jump 4 indices.

class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        i = 0
        while i < len(command):
            if command[i]=="G":
                ans.append('G')
                
            elif command[i]=='(' and command[i+1]==')':
                ans.append('o')
                i+=2
                continue
            else:
                ans.append("al")
                i+=4
                continue
            i+=1
        return ''.join(ans)