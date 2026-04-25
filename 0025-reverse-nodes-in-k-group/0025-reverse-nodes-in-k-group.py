# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        last = ListNode(0)
        ll = head
        #check the length of linked list
        dummy = head
        size = 0
        while dummy:
            size += 1
            dummy = dummy.next
        #break the linked list into part where each part is of k length and save those parts in list names as arr
        count = 0
        while ll:
            count +=1
            if count % k ==0:
               temp = head
               head = ll.next
               ll.next = None
               ll = head
               size -=k
               arr.append(temp)
               continue
            if size < k:
                break
            ll = ll.next
        #reverse those parts of linked list (arr[i])
        for i in range(len(arr)):
            node = arr[i]
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            arr[i] = prev
        #join all arr[i] and ll(the last left part)
        ans = ListNode(0)
        res = ans
        for i in arr:
            res.next = i
            while res.next:
                res = res.next
        res.next = ll
        return ans.next
        

        