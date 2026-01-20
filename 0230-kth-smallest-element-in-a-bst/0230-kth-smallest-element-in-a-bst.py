# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        
        
        self.count = 0
        def dfs(node):
            if node is None:
                return None

            left = dfs(node.left)
            if left is not None:
                return left
                
            self.count += 1
            if self.count == k:
                return node.val

            right = dfs(node.right)
            if right is not None:
                return right


        return dfs(root)

        

        