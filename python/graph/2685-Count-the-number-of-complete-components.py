# Problem: Leetcode 2685 - Count the number of complete components
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-the-number-of-complete-components/description/
# Time Complexity: O(n+e) which is standard bfs time complexity as we have nodes and edges
# Space Complexity: O(n+e) as we construct the graph for bfs and the queue
# Approach: We simply perform DFS and for each node in graph if its not visited we start a new queu to visit all of its neighbours
# and we start a count to count the nodes and edges that we will find. after the loop if over we divided edges by 2 
# as its undirected graph so edge count must be double that actual edges. then we use the main mathematical formula
# that if the edges found during bfs of a node is equal to number of adjacent nodes * ( number of adj nodes - 1) //2
# then its a complete component in itself and we increment our count by 1

from typing import List
from collections import deque
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        def bfs(graph,visited):
            complete_count = 0
            for i in range(n):
                if not visited[i]:
                    q = deque([i])
                    visited[i] = True
                    num_nodes = 0
                    num_edges = 0
                    while q:
                        node = q.popleft()
                        num_nodes+=1
                        num_edges+=len(graph[node])
                        for nei in graph[node]:
                            if not visited[nei]:
                                visited[nei]= True
                                q.append(nei)
                    num_edges //= 2
                    if num_edges == num_nodes * (num_nodes - 1) // 2:
                        complete_count += 1
            return complete_count
        

        #construct graph
        adj_list= [[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * n
        return bfs(adj_list,visited)#immutable integer so dont pass a pattern here
