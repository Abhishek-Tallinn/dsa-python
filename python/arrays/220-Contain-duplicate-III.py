# Problem: Leetcode 220 - Contains Duplicate III
# Difficulty: Hard
# Link: https://leetcode.com/problems/contains-duplicate-iii/description/
# Time Complexity: O(n) - as we are iterating through the list once
# Space Complexity: O(k) as we store at most k elements in the buckets
# Approach: We use a bucketing technique to efficiently check for nearby almost duplicates. We make buckets and if a bucket already exits or if element in nearby bucket is within the valueDiff we can return True as the window we keep valid.
# Approach 2: we use a BST/ordered window using SortedList where we keep every window sorted and in indexDiff range. then we find pos to new element to be inserted and if its withing valueDiff of its nearby neighbouts(since window is sorted and nearby neighbour will have the least valueDiff so highest change of being withing the valueDiff)
# we just return True.
# Question is very easy if we are allowed an O(n^2) approach but that leads to TLE.


from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        buckets = {}
        size = valueDiff + 1

        for i, num in enumerate(nums):

            bucket_id = num // size

            # same bucket
            if bucket_id in buckets:
                return True

            # left bucket
            if (
                bucket_id - 1 in buckets and
                abs(num - buckets[bucket_id - 1]) <= valueDiff
            ):
                return True

            # right bucket
            if (
                bucket_id + 1 in buckets and
                abs(num - buckets[bucket_id + 1]) <= valueDiff
            ):
                return True

            buckets[bucket_id] = num #key is the index

            # maintain sliding window
            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_bucket = old_num // size
                del buckets[old_bucket]

        return False


        '''Ordered BST window solution
        from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(
        self,
        nums,
        indexDiff,
        valueDiff
    ):

        window = SortedList()

        for i, num in enumerate(nums):

            # find insertion position
            pos = window.bisect_left(num)

            # check right neighbor
            if (
                pos < len(window) and
                abs(window[pos] - num) <= valueDiff
            ):
                return True

            # check left neighbor
            if (
                pos > 0 and
                abs(window[pos - 1] - num) <= valueDiff
            ):
                return True

            window.add(num)

            # maintain sliding window
            if len(window) > indexDiff:
                window.remove(nums[i - indexDiff])

        return False
        
        
        '''
