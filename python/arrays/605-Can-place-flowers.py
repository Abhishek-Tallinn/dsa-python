# Problem: Leetcode 605 - Can Place Flowers
# Difficulty: Easy
# Link: https://leetcode.com/problems/can-place-flowers/description/
# Time Complexity: O(n) as we iterate through the flowerbed once
# Space Complexity: O(1) as we only use a constant amount of extra space
# Approach: We iterate through flowerbed and for each empty spot we checks its neighbours and if spot is empty and both neighbours are empty we plant a flower there
# and we update the flowerbed and also the cnt. then if we return if cnt >=n meaning that we can consume all the n flowers

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                continue
            left = flowerbed[i-1] if i>0 else 0
            right = flowerbed[i+1] if i< len(flowerbed)-1 else 0
            if left == 0 and right == 0:
                cnt+=1
                flowerbed[i]=1
        return cnt>=n
        '''
        cnt=0
        if len(flowerbed)==1:
            return n <= flowerbed.count(0)
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                cnt+=1
            if i == len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0:
                flowerbed[i]=1
                cnt+=1
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                cnt+=1
        return cnt >= n
        '''