# Problem: Leetcode 3581 - Count odd letters from number
# Difficulty: Easy
# Link: https://leetcode.com/problems/Count-odd-letters-from-number/description/
# Time Complexity: O(k) where k is the total number of digits in n
# Space Complexity: O(k + L) where L<=5k where k is total characters
# Approach: We make a hashmap of numbers mapped to their string value. then we loop over digits of the number and add their word value to a list which we join to a string.
# List is used to avoid creating a new string everytime. Then we convert it to a hashmap to see frequencies and then we could the number of odd values and return the count.


from collections import Counter
class Solution:
    def countOddLetters(self, n: int) -> int:
        num_map = {
            0 : "zero",
            1 : "one",
            2 : "two",
            3 : "three",
            4 : "four",
            5 : "five",
            6 : "six",
            7 : "seven",
            8 : "eight",
            9 : "nine"
        }
       
        res = []
        while n > 0:
            digit = n%10
            res.append(num_map[digit])
            n=n//10
        s = ''.join(res)
        d = Counter(s)
        cnt = 0
        for value in d.values():
            if value%2==1:
                cnt+=1
        return cnt

        '''
        counter = Counter()

        while n > 0:
            counter.update(num_map[n % 10])
            n //= 10

        return sum(freq % 2 for freq in counter.values())
        '''