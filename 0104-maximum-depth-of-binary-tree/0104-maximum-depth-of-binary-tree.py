# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    
        def dfs(node):
            # Base case: if node is ???
            if node is None :
                return 0 
            # Get left and right heights
            left = dfs(node.left)
            right = dfs(node.right)
            
            
            # Return height of this subtree
            return 1 + max(left, right)
        
        res = dfs(root)
        return res
