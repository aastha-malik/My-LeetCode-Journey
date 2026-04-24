# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) > 0:
            dummy = lists[0]
            for i in range(1, len(lists)):
                head = ListNode(0)
                ll = head
                node = lists[i]
                while dummy and node:

                    if dummy.val > node.val:
                        ll.next = node
                        node = node.next

                    elif dummy.val <= node.val:
                        ll.next = dummy
                        dummy = dummy.next
                    ll = ll.next
                if dummy:
                    ll.next = dummy
                if node:
                    ll.next = node
                dummy = head.next
            return dummy
