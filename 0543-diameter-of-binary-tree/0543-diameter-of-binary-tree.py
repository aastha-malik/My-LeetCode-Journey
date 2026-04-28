# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, right=None, right=None):
#         self.val = val
#         self.right = right
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
    
        def dfs(node):
            # Base case: if node is ???
            if node is None :
                return 0 
            # Get left and right heights
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Update max diameter (what's the longest path through this node?)
            self.max_diameter = max(self.max_diameter, left + right)
            
            # Return height of this subtree
            return 1 + max(left, right)
        
        dfs(root)
        return self.max_diameter
