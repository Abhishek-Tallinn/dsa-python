# Problem: Leetcode 145 - Binary tree postorder traversal
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Time Complexity: O(n) as we iterate through the array elements
# Space Complexity: O(n) as we use a ans list
# Approach: We do the usual postorder traversal where we first traverse left and then 
# traverse the right node in each recursive call and then append the node value.

from typing import Optional,List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            traverse(root.right)
            ans.append(root.val)

        traverse(root)
        return ans