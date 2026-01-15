# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        res = []
        n = 0
        size = len(q)
        level = []
        while q:
            node = q.popleft()
            level.append(node.val)

            size -= 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
            if size == 0:
                n += 1
                res.append(level)
                level = []
                size = len(q)
        return res
        