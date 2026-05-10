# Problem: Leetcode 1306 - Jump game 3
# Difficulty: Medium
# Link: https://leetcode.com/problems/jump-game-III/description/
# Time Complexity: O(n) as we iterate over the values of the array
# Space Complexity: O(n) as we create the visited set which can be the size of array in worst case
# Approach: Since each index from start can lead us to multiple indices(or nodes) and each nodes represents a state from which we can reach different states depending on our decision
# Hence, it is intuitive that it is a graph problem. A simple graph is employed and after construction dfs function is called. If the element of 0 which could be any element is found,
# we immediately return true


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(node,visited):
            if arr[node] == 0:
                return True
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor,visited):
                    return True
            return False
            

        graph = [[] for _ in range(len(arr))]
        for i in range(len(arr)):
            if i + arr[i]<=len(arr)-1:
                graph[i].append(i+arr[i])
            if i-arr[i]>=0:
                graph[i].append(i-arr[i])
        #graph created now start the dfs
        
        visited = set()
        return dfs(start,visited)
