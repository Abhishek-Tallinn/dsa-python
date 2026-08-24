# Problem: Leetcode 2525 - Categorize box according to criteria
# Difficulty: Easy
# Link: https://leetcode.com/problems/categorize-box-according-to-criteria/description/
# Time Complexity: O(1) - constant time operations
# Space Complexity: O(1) - constant space usage
# Approach: We add box features to an array and based on array length we return its category

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        mx = 10**4
        features = []
        ans = ""
        if any(i >= mx for i in (length,width,height,mass)) or length*width*height>=10**9:
            features.append("Bulky")
        if mass>=100:
            features.append("Heavy")
        if len(features)==2:
            return "Both"
        if not features:
            return "Neither"
        if len(features)==1:
            if features[0]=="Bulky":
                return "Bulky"
            else:
                return "Heavy"
        