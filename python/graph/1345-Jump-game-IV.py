# Problem: Leetcode 1345 - Jump game IV
# Difficulty: Hard
# Link: https://leetcode.com/problems/jump-game-IV/description/
# Time Complexity: O(n) as we iterate over the values of the graph and use clear method to avoid iterating over the same values again. So we dont revisit any node.
# Space Complexity: O(n) as we create the graph and the visited set and the queue but total space used is O(n)
# Approach: The problem involved BFS on a graph as BFS on each node level guarantees that you visit the node in the least number of steps. However, we need to optimize the BFS with clear the visited nodes after each iteration 
# to avoid revisiting the nodes and avoid time limit exceeded. Also, we use a inner FOR loop inside the usual while loop in BFS and first traverse all the neighbour of a node to see if we reach the target
# if we do we just return the total number of steps but if we dont then we added 1 to steps and move to next node.

from typing import list

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        def bfs(node,visited,steps,target):
            q = deque([node])
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if node == target:
                        return steps
                    neighbours = []
                    neighbours.extend([node-1,node+1]) 
                    neighbours.extend(graph[arr[node]])

                    for neighbour in neighbours:
                        if 0<=neighbour<len(arr) and neighbour not in visited:
                            q.append(neighbour)
                            visited.add(neighbour) 
                    graph[arr[node]].clear()
                steps+=1
            return -1

        if len(arr)==1:
            return 0
        steps=0
        target = len(arr)-1
        graph = defaultdict(list)   
        for i,val in enumerate(arr):
            graph[val].append(i)
        visited = set([0])
        return bfs(0,visited,steps,target)
        