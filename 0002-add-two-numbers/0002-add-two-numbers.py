# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        p1 = None
        c1 = l1
        while c1:
            temp = c1.next
            c1.next = p1
            p1 = c1
            c1 = temp
        while p1:
            s1 += str(p1.val)
            p1 = p1.next

        s2 = ""
        p2 = None
        c2 = l2
        while c2:
            temp = c2.next
            c2.next = p2
            p2 = c2
            c2 = temp
        while p2:
            s2 += str(p2.val)
            p2 = p2.next


        s = str( int(s1) + int(s2) )
        # 8 0 7
        head = ListNode(0)
        ll = head
        for i in range(len(s)-1, -1, -1):
            ll.val = int(s[i])
            if i != 0:
                ll.next = ListNode(0)
                ll = ll.next
        return head
