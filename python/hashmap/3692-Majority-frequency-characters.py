# Problem: Leetcode 3692 - Filter characters by frequency
# Difficulty: Easy
# Link: https://leetcode.com/problems/filter-characters-by-freq/description/
# Time Complexity: O(n+k) for first approach and O(n+k log k) for second approach
# Space Complexity: O(k) where k is the size of hashmap
# Approach1: We simply make a hashmap of s to get frequencies. Then with freq as key and character lists as values we make another hashmap to find our answer. then we can use two approaches. In first approach,
# we simply take best_chars and best_freq variable and we iterate over the dictionary made from dictionary of the original string and keep 
# updating best chars and best freq as per constraints. if best_chars len is equal to current chars we compare with freq and update accordingly.
# Approach2: in approach 2 making dictionary process is same. but we sort the dictionary in reverse so highest frequency(key) is at top. then we iterate on this sorted dictionary
# and only when a value of chars which has higher length than the best length is found we update the best chars and at the end we 
# return the length of the chars in the answer array.


from collections import Counter

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        d = Counter(s)
        d1 = {}
        for key,value in d.items():
            if value in d1:
                d1[value].append(key)
            else:
                d1[value] = [key]
        best_chars = []
        best_freq = 0
        for freq,chars in d1.items():
            if (len(chars) > len(best_chars)) or (len(chars)==len(best_chars) and freq>best_freq):
                best_chars = chars
                best_freq = freq
        return ''.join(best_chars)
        '''
        d2 = dict(sorted(d1.items(),key=lambda x:x[0], reverse = True))
        ans = []
        mx = 0
        for key,value in d2.items():
            if len(value) > mx:
                mx = len(value)
                if ans:
                    ans.pop()
                ans.append(value)
        res = ''.join(ans[0])
        return res
        '''