# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        if p is None and q is None:
            return True
        else:
            p_deque = deque([p])
            q_deque = deque([q])

            while p_deque and q_deque:
                node_p = p_deque.popleft()
                node_q = q_deque.popleft()

                if node_p.val != node_q.val:
                    return False
                if node_p.left and node_q.left:
                    p_deque.append(node_p.left)
                    q_deque.append(node_q.left)
                if node_p.left is None and node_q.left is not None:
                    return False
                if node_p.left is not None and node_q.left is None:
                    return False
                
                if node_p.right and node_q.right:
                    p_deque.append(node_p.right)
                    q_deque.append(node_q.right)
                if node_p.right is None and node_q.right is not None:
                    return False
                if node_p.right is not None and node_q.right is None:
                    return False
            return True
                