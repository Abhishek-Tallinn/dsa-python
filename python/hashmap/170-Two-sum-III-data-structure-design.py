# Problem: Leetcode 170 - Two Sum III data structure design
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum-iii-data-structure-design/description/
# Time Complexity: O(1) for add and O(n) for find
# Space Complexity: O(n) as we use the dictionary data structure
# Approach1: simple implementation with a list where add is O(1) but find is O(nlogn) and binary search is used to find the pair
# Approach2: using hashmap where add is O(1) and find is reduced to O(n) but checking the complement in the dictionary.
# we can also opt for a slow add and fast find function by precomputing all pair total and adding it in a set or dictionary to make find O(1).


from collections import defaultdict
class TwoSum:

    def __init__(self):
        #self.nums = []
        self.freq = defaultdict(int)
        

    def add(self, number: int) -> None:
        #self.nums.append(number)
        self.freq[number]+=1

    def find(self, value: int) -> bool:
        for x in self.freq:
            y = value - x
            if x == y:
                if self.freq[x]>=2:
                    return True
            elif y in self.freq:
                return True
        return False
        '''
        self.nums.sort()
        for i in range(len(self.nums)-1):
            left = i+1
            right = len(self.nums)-1
            while left<=right:
                mid = (left+right)//2
                if self.nums[i]+self.nums[mid]==value:
                    return True
                elif self.nums[i]+self.nums[mid]>value:
                    right = mid-1
                else:
                    left = mid+1
        return False
       '''
