# Problem: Leetcode 2437 - Number of Valid Clock Times
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-valid-clock-times/description/
# Time Complexity: O(1) - constant time operations
# Space Complexity: O(1) - constant space usage
# Approach: We analyze each position of the time string and calculate the number of valid possibilities for hours and minutes separately, then multiply them.
# Due to many different possibilities we use helper function to calculate and return the total possibilities.



class Solution:
    def countTime(self, time: str) -> int:
        
        def hour_possible(hour)->int:
            total = 1
            if hour=='??':
                total*=24
            elif hour[0]=='?':
                if int(hour[1]) < 4:
                    total*=3
                
                else:
                    total*=2
            elif hour[1]=='?':
                if int(hour[0])<2:
                    total*=10
                else:
                    total*=4
            return total
        def mins_possible(mins):
            total = 1
            if mins=="??":
                total*=60
            elif mins[0]=='?':
                total*=6
            elif mins[1]=='?':
                total*=10
            return total
        hour,mins = time.split(":")
        h = hour_possible(hour)
        m = mins_possible(mins)
        return h*m