/* 
Problem: Leetcode 2255 - Count prefixes of a given string
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-prefixes-of-a-given-string/description/
# Time Complexity: O(n) - as we iterate on words
# Space Complexity: O(k) as we make a temporary substring
# Approach: We iterate through the words and for each word we slicing the string with length equal to the len of word and compare.
*/

class Solution {
    public int countPrefixes(String[] words, String s) {
        int cnt = 0;
        for (String word:words){
            int n = word.length();
            if (s.substring(0,Math.min(n,s.length())).equals(word)) {cnt++;}
        }
        return cnt;
    }
}