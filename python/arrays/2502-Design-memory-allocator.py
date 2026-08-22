# Problem: Leetcode 2502 - Design memory allocator
# Difficulty: Medium
# Link: https://leetcode.com/problems/design-memory-allocator/description/
# Time Complexity: O(n) per call
# Space Complexity: O(1) as we only use two pointers
# Approach: We use the pointer approach and check blocks to see if there is enough space to allocate memory otherwise we keep jumping blocks
# then for freeing memory also we check each MID and keep incrementing inner pointer to free up blocks of the particular mID
# and then we keep jumping the pointer pas the block

class Allocator:

    def __init__(self, n: int):
        self.memo = [-1]*n
        
    def allocate(self, size: int, mID: int) -> int:
        i = 0
        while i < len(self.memo):
            j=i
            while j < len(self.memo) and self.memo[j] == -1:
                j+=1
            if j-i >= size:
                for k in range(i,i+size):
                    self.memo[k] = mID
                return i
            i = j+1
        return -1

    def freeMemory(self, mID: int) -> int:
        total=0
        i = 0
        while i < len(self.memo):
            if self.memo[i] == mID:
                j = i
                while j<len(self.memo) and self.memo[j]==mID:
                    j+=1
                #assign
                for k in range(i,j):
                    self.memo[k] = -1
                    total+=1
                i=j+1
                continue
            i+=1
        return total
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)