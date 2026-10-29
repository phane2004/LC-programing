# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        prev, curr = dummy, head
        
        while curr and curr.next:
            ctail = curr.next.next
            nxt = curr.next

            nxt.next = curr
            curr.next = ctail
            prev.next = nxt

            prev = curr
            curr = ctail
        return dummy.next
            