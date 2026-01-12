# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        if len(lists) > 0:

            res = lists[0]

            for i in range(1, len(lists)):
                dummy = ListNode(0)
                ll = dummy

                first = res
                second = lists[i]

                while first and second :
                    
                    if first.val <= second.val:
                        ll.next = first
                        first = first.next

                    else:
                        ll.next = second
                        second = second.next
                    ll = ll.next

                if first :
                    ll.next = first
                if second :
                    ll.next = second

                res = dummy.next
            return res
            
            