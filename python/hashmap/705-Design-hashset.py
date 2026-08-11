# Problem: Leetcode 705 - Design HashSet
# Difficulty: Easy
# Link: https://leetcode.com/problems/design-hashset/description/
# Time Complexity: O(n) worst case 
# Space Complexity: O(n) 
# Approach: We use a boolean array to represent the presence of each key.
# Appraoch2: we can also do it bucket wise where each bucket is a list of lists and stores the keys.


class MyHashSet:

    def __init__(self):
        #self.set = [[]*10003]
        self.set = [False]*(10**6+1)
        

    def add(self, key: int) -> None:
        self.set[key] = True
        #h = hash(key)
        #index = h%len(self.set)
        #if key not in self.set[index]:
        #    self.set[index].append(key)
        
    def remove(self, key: int) -> None:
        self.set[key] = False
        #h = hash(key)
        #index = h%len(self.set)
        #if key in self.set[index]:
        #    self.set[index].remove(key)
        

    def contains(self, key: int) -> bool:
        return self.set[key]
        #h = hash(key)
        #index = h % len(self.set)
        #return key in self.set[index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)