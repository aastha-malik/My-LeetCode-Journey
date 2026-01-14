# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p  and q is None:
            return False
        if p is None and q:
            return False

        
        p_que = deque([p])
        q_que = deque([q])

        while p_que and q_que:
            p_node = p_que.popleft()
            q_node = q_que.popleft()

            if p_node.val != q_node.val:
                return False
            if p_node.left and q_node.left:
                if p_node.left:
                    p_que.append(p_node.left)
                if q_node.left:
                    q_que.append(q_node.left)
            else:
                if p_node.left and q_node.left is None:
                    return False
                if p_node.left is None and q_node.left :
                    return False
            
            if p_node.right and q_node.right:
                if p_node.right:
                    p_que.append(p_node.right)
                if q_node.right:
                    q_que.append(q_node.right)
            
            else:
                if p_node.right and q_node.right is None:
                    return False
                if p_node.right is None and q_node.right :
                    return False
        return True
