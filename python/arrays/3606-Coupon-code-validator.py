# Problem: Leetcode 3606 - Coupon code validator
# Difficulty: Easy
# Link: https://leetcode.com/problems/coupon-code-validator/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) as we store the list
# Approach: We perform all the checks on each code and take only valid codes into the valid array. Then we
# sort them as per our custom defined order dictionary and then we extra the coupons once its sorted
# We use tuple based sorting as sorting has to be done on multiple criteria

from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        def checkCode(c) -> bool:
            for char in c:
                if not char.isalnum():
                    if char!='_':
                        return False
            return True
        valid = []
        validLines = ('electronics','grocery','pharmacy','restaurant')
        for i,c in enumerate(code):
            if not c or not checkCode(c) or businessLine[i] not in validLines or not isActive[i]:
                continue 
            valid.append((c,businessLine[i]))
        valid.sort(key=lambda x:(order.get(x[1],999),x[0]))
        res = [coupon for coupon,cat in valid]
        return res