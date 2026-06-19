# Problem: Leetcode 1736 - Latest time by replacing hidden digits
# Difficulty: Easy
# Link: https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/description/
# Time Complexity: O(1) as we only move through 5 characters
# Space Complexity: O(1) 
# Approach: We simply check where the ? appears and check the preceding character or succeeding number and accordingly fill the greatest number possible to get the latest time.



class Solution:
    def maximumTime(self, time: str) -> str:
        new_time=[]
        for i in range(len(time)):
            if time[i]=='?':
                if i==0:
                    if time[i+1]!='?' and int(time[i+1])>=4:
                        new_time.append('1')
                    else:
                        new_time.append('2')
                elif i==1:
                    if time[i-1]=='0' or time[i-1]=='1':
                        new_time.append('9')
                    elif time[i-1]=='2':
                        new_time.append('3')
                    else:
                        new_time.append('3')
                elif i==3:
                    new_time.append('5')
                elif i==4:
                    new_time.append('9')

            else:
                new_time.append(time[i])
        return ''.join(new_time)