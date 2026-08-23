# Problem: Leetcode 94 - Binary tree inorder traversal
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Time Complexity: O(n) as we iterate through the array elements
# Space Complexity: O(n) as we use a ans list
# Approach: We do the usual inorder traversal where we traverse left and then append the value 
# and then traverse right node in each recursive call

from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(root):
            if not root:
                return 
            traverse(root.left)
            ans.append(root.val)
            traverse(root.right)
        traverse(root)
        return ans