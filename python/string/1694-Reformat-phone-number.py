# Problem: Leetcode 1694 - Reformat phone number
# Difficulty: Easy
# Link: https://leetcode.com/problems/reformat-phone-number/description/
# Time Complexity: O(n) as we perform join operations
# Space Complexity: O(n) 
# Approach: We iterate in hops of 3 and and take the elements together. if i reaches an index after which 4 or less elements are left we break
# then we check exactly how many are left. If 2 or 3 which just collect them in one slice. If 4 then we collect them in two slices
# then we finally join them together and return the answer.
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = [char for char in number if char!=' ' and char!='-']
        ans = []
        res = []
        start = 0
        for i in range(0,len(number),3):
            if len(number)-i <= 4:
                start = i
                break
            ans.append(number[i:i+3])
            ans.append('-')
            
        if len(number)-i == 4:
            ans.append(number[i:i+2])
            ans.append('-')
            ans.append(number[i+2:])
        else:
            ans.append(number[i:])
        
        for i in ans:
            res.append(''.join(i))
        return ''.join(res)