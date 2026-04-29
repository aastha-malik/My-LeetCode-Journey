# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            if subRoot is None:
                return  True
            else:
                return False
        if subRoot is None and root is not None:
            return True
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                p_deque = deque([node])
                q_deque = deque([subRoot])
                broke = False

                while p_deque and q_deque:
                    node_p = p_deque.popleft()
                    node_q = q_deque.popleft()

                    if node_p.val != node_q.val:
                        broke = True
                        break
                    if node_p.left and node_q.left:
                        p_deque.append(node_p.left)
                        q_deque.append(node_q.left)
                    if node_p.left is None and node_q.left is not None:
                        broke = True
                        break
                    if node_p.left is not None and node_q.left is None:
                        broke = True
                        break
                    
                    if node_p.right and node_q.right:
                        p_deque.append(node_p.right)
                        q_deque.append(node_q.right)
                    if node_p.right is None and node_q.right is not None:
                        broke = True
                        break
                    if node_p.right is not None and node_q.right is None:
                        broke = True
                        break
                if broke == True:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    return True
            else:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False
                    