# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(node):
            if node is None:
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            if left == False or right == False:
                return False
            
            diff = abs(left - right)
            if diff > 1:
                return False
            return 1 + max(left, right)
        res = dfs(root)
        return res != False
        
