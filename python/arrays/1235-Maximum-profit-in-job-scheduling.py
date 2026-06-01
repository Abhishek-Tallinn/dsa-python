# Problem: Leetcode 1235 - Maximum Profit in Job Scheduling
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
# Time Complexity: O(n log n) due to sorting and binary search
# Space Complexity: O(n) for the dynamic programming array
# Approach: Sort jobs by end time and use dynamic programming with binary search to find the latest non-overlapping job. Once we find it with bisec_left for suffixDP(reverse) or bisect_right for prefixDP(forward)
# then we can either take the current job or skip the current job by taking dp[i+1] value or for current job we take its profit + dp[nxt] with nxt represeting the job which would have immediately followed it.

from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime,endTime,profit))
        jobs.sort(key = lambda x: x[1])
        ends = [job[1] for job in jobs]
        n = len(startTime)
        dp = [0] * n
        for i in range(n):
            start,end,profit = jobs[i]
            j = bisect_right(ends,start)-1
            take = profit
            if j >= 0:
                take+=dp[j]
            skip = dp[i-1] if i>0 else 0
            dp[i]= max(skip,take)
        return dp[-1] #max profit collects at end
        '''
        jobs = sorted(zip(startTime,endTime,profit))
        starts = [s[0] for s in jobs]
        n = len(startTime)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            start,end,profit = jobs[i]
            nxt = bisect_left(starts,end) 
            dp[i] = max(dp[i+1], profit+dp[nxt])
        return dp[0]
        '''

        