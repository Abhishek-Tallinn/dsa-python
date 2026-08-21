# Problem: Leetcode 3116 - kth smallest amount with single denomination combination
# Difficulty: Hard
# Link: https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/description/
# Time Complexity: O(n log n)
# Space Complexity: O(1) 
# Approach: We use binary search to see if k elements exist for a mid value. for each mid value we calculate the total count of elements upto this value.
# this count is not linear dependent on just multiples of each element in the current subset as repeated elements are removed. What to remove is calculated 
# by using a bitmask to generate different subsets and for different subsets we calculate the lcm value and then using 
# the inclusion-exclusion principle we remove the elements that are repeating. If the subset length is even the contribution is removed and its its odd then the contributions is 
# added as per the set union and intersection formula
# we keep shrinking the search speace and if a mid is possible we store it in first_valid_index and return it at the end
from typing import List
from math import lcm

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count_multiples_up_to(max_value: int) -> int:
            
            total_count = 0

            # Iterate through all non-empty subsets of coins using bitmask
            for subset_mask in range(1, 1 << len(coins)):
                lcm_value = 1

                # Calculate LCM of all coins in current subset
                for coin_index, coin_value in enumerate(coins):
                    if subset_mask >> coin_index & 1:
                        lcm_value = lcm(lcm_value, coin_value)
                        if lcm_value > max_value:
                            break

                # Apply inclusion-exclusion principle
                subset_size = subset_mask.bit_count()
                if subset_size & 1:
                    total_count += max_value // lcm_value
                else:
                    total_count -= max_value // lcm_value

            return total_count

        def feasible(mid: int) -> bool:
            """Check if there are at least k valid amounts <= mid."""
            return count_multiples_up_to(mid) >= k

        # Binary search using the standard template
        left, right = 1, 10**11
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_true_index