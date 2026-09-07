# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        def rec(curr, n):
            if curr == None:
                return None

            curr.next = rec(curr.next, n)
            n[0] -= 1
            if n[0] == 0:
                return curr.next
            return curr
        
        return rec(head, [n])