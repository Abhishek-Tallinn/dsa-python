# Problem: Leetcode 362- Design hit counter
# Difficulty: Medium
# Link: https://leetcode.com/problems/design-hit-counter/description/
# Time Complexity: O(1) as we only iterate over fixed 300 values
# Space Complexity: O(n) as we use the hashmap
# Approach1: We initialize a default dict of int and for every timestamp we enter it into the hashmap
# when getHits is called we iterate from timestamp - 299 to timestamp and add the count of the timestamp if its in the hashmap.

from collections import defaultdict
class HitCounter:

    def __init__(self):
        self.record = defaultdict(int)
        

    def hit(self, timestamp: int) -> None:
        self.record[timestamp]+=1

    def getHits(self, timestamp: int) -> int:
        start = max(0,timestamp-300) + 1
        total = 0
        for i in range(start,timestamp+1):
            total += self.record[i]
        return total

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)