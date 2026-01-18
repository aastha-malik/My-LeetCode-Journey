# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


        stack = [root]
        
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                # sametree func logic in dfs...
                
                if isSameTree(node, subRoot):
                    return True

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return False

        