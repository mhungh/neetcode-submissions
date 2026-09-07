# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

            
        dummy = head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #rev
        curr = slow.next
        slow.next = None
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, sec = head, prev
        while sec:
            tmp1, tmp2 = first.next, sec.next
            first.next = sec
            sec.next = tmp1
            first, sec = tmp1, tmp2



