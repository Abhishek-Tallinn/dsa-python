# Problem: Leetcode 144 - Binary tree preorder traversal
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Time Complexity: O(n) as we iterate through the array elements
# Space Complexity: O(n) as we use a ans list
# Approach: We do the usual preorder traversal where we first append the root and then traverse left and then 
# and then traverse the right node in each recursive call


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional,List

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(root):
            if not root:
                return
            ans.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return ans