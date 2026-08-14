# Problem: Leetcode 4014 - Minimum total price after applying discounts
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-total-price-after-applying-discounts/description/
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Approach: We reverse sort and apply the largest discounts on the largest price and add the remaining element for which no discount was applied.


class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse = True)
        discounts.sort(reverse=True)
        total = 0
        k = 0
        for price in prices:
            if k==len(discounts):
                break
            total += price * (100-discounts[k])/100
            k+=1
        total += sum(prices[k:])
        return total