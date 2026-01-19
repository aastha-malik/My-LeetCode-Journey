# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isBst(root, min_val, max_val):
            if root is None:
                return True
            if root :
                if not (min_val < root.val  < max_val):
                    return False
                return isBst(root.left, min_val, root.val) and isBst(root.right, root.val, max_val)
            

                


        
        return isBst(root, float('-inf'), float('inf')) 

