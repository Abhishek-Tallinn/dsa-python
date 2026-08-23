# Problem: Leetcode 1927 - Sum game
# Difficulty: Medium
# Link: https://leetcode.com/problems/sum-game/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Its a math problem. We need to check if sum difference between two halves is equal to 9 times the 
# half value of the question mark difference the opposite way. It if is then bob can balance and we return False 
# else alice will win. also if total question marks is off alice always wins.

class Solution:
    def sumGame(self, num: str) -> bool:
        #count in first half
        cnt1 = cnt2=0
        s1 = s2 = 0
        for i in range(len(num)//2):
            if num[i]=='?':
                cnt1+=1
            else:
                s1+=int(num[i])
        for i in range(len(num)//2,len(num)):
            if num[i]=='?':
                cnt2+=1
            else:
                s2+=int(num[i])
        #if cnt1==0 and cnt2==0:
        #    return s1!=s2 
        if (cnt1+cnt2)%2==1 or s1-s2!=9*(cnt2-cnt1)//2:
            return True
        return False