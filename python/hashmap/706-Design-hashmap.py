# Problem: Leetcode 706 - Design HashMap
# Difficulty: Easy
# Link: https://leetcode.com/problems/design-hashmap/description/
# Time Complexity: O(n) worst case 
# Space Complexity: O(n) 
# Approach: We convert to each key during put to a hash and insert it into out hashmap list of lists.
# while getting we calculate index the same way and get the value. While initializing the hashmap we can use a prime number size
# so that while calculating index the collisions are minimized. 


class MyHashMap:

    def __init__(self):
        self.map = [[] for _ in range(10000)]
        

    def put(self, key: int, value: int) -> None:
        h = hash(key)
        index = h % len(self.map)
        for i,(k,v) in enumerate(self.map[index]):
            if k == key:
                self.map[index][i][1] = value
                return
        self.map[index].append([key,value])
    

    def get(self, key: int) -> int:
        h = hash(key)
        index = h % len(self.map)
        for k,v in self.map[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = hash(key)
        index = h % len(self.map)
        self.map[index] = [[k,v] for k,v in self.map[index] if k!=key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)