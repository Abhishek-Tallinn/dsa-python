# Problem: Leetcode 3499 - Maximize active section after trade
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximize-active-section-after-trade/description/
# Time Complexity: O(n) as we effectively make one pass over array
# Space Complexity: O(1) as we only work with variables
# Approach: We iterate throught the string and keep jumping while counting segments. If the segment belong to 1's we just increment our total count of ones
# if the segments if of 0s we count the max zeros we can gain from this section and the previous zero segment that we have seen
# because that means we found a 0 segment and this can match with another zero segment before as the 1's between them will first be converted to a zero
# we dont need to actually convert anything as at the end we just add total ones and mx zeros we can gain as the temporary 1 that we will 
# convert to 0 will also come back to us and hence total ones at the end will be the total of actual ones and how many zeros we can gain


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        total_ones = 0
        index = 0
        prev_zero_segment = float('-inf')
        mx_zero_gain = 0
        while index < n:
            segment_end = index+1
            while segment_end < n and s[segment_end] == s[index]:
                segment_end+=1
            
            curr_segment_length = segment_end - index
            if s[index]=='1':
                total_ones += curr_segment_length
            else:
                mx_zero_gain = max(mx_zero_gain,prev_zero_segment + curr_segment_length)
                prev_zero_segment = curr_segment_length
            index = segment_end

        return (total_ones + mx_zero_gain)