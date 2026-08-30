# Problem: Leetcode 2303 - Calculate amount paid in taxes
# Difficulty: Easy
# Link: https://leetcode.com/problems/calculate-amount-paid-in-taxes/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we create new Nums
# Approach: We just check income against each bracket and keep track of previous bracket to calculate the amount on which tax is levied.
# so if income is greater than bracket upper amount, we calcualte tax and keep moving and keep updating our prev variable.
# if income is less than upper we simply calculate tax on income - prev and break as this is the last bracket.
# then we return tax

from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        prev = 0
        for i in range(len(brackets)):
            if income > brackets[i][0]:
                tax += ((brackets[i][0]-prev)*brackets[i][1])/100
            else:
                tax+= ((income - prev)*brackets[i][1])/100
                break
            prev = brackets[i][0]
        return tax