# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
        curr = head
        count = 1
        while curr.next != None:
            curr = curr.next
            count += 1
        curr.next = head
        k = k % count
        res = count - k
        
        while res > 0:
            head = head.next
            res -= 1

        curr = head
        while curr.next != head:
            curr = curr.next
        curr.next = None
        return head
        