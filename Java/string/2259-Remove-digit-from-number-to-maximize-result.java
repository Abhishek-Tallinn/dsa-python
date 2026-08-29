/* 
Problem: Leetcode 2259 - Remove digit from number to maximize result
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/
# Time Complexity: O(n) - as we iterate on words
# Space Complexity: O(k) as we make a temporary substring
# Approach: We just compare string lexicographically after removing each digit
*/

class Solution {
    public String removeDigit(String number, char digit) {
        String mx = "";
    for (int i = 0; i < number.length(); i++) {
        if (number.charAt(i)==digit){
             String candidate = number.substring(0, i) + number.substring(i + 1);
            if (mx.isEmpty() || candidate.compareTo(mx) > 0) {
            mx = candidate;
            }
        }
    }
    return mx;
    }
} 
    

