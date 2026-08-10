# Problem: Leetcode 697 - Degree of an Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/degree-of-an-array/description/
# Time Complexity: O(n) as we iterate through the array once
# Space Complexity: O(n) as we use a dictionary to store the frequency of each element
# Approach: We find the degree of an array and by find the max frequency and record the first and last freq of each element of array
# then while iterating through the freq dictionary we check if its the key with max freq and we calculate the length of the subarray.

from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        last = {}
        freq = {}
        for i,num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            freq[num] = freq.get(num,0)+1
        degree = max(freq.values())
        mn = float('inf')
        for num in freq:
            if freq[num] == degree:
                mn = min(mn,last[num]-first[num]+1)
        return mn


        '''
        d = Counter(nums)
        degree = max(d.values())
        if degree==1:
            return 1
        targets = []
        for num,freq in d.items():
            if freq == degree:
                targets.append(num)
        mn = float('inf')
        for num in targets:
            start=end=0
            seen = False
            for i in range(len(nums)):
                if nums[i] == num:
                    if not seen:
                        start=i
                        seen = True
                    else:
                        end = i

            mn = min(mn,end-start+1)
        return mn
        '''
