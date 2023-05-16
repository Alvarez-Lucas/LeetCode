from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Traverse recursively, swapping as you go down, return the root node at the end
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case, if no root, return
        if not root:
            return None

        # Swap
        tmp = root.left
        root.right = root.left
        root.right = tmp

        # Visit children
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the head
        return root
