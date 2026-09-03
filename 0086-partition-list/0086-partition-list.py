# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        less = []
        more = []
        curr = head
        while curr != None:
            if curr.val < x:
                less.append(curr.val)
            else:
                more.append(curr.val)
            curr = curr.next
        curr = head
        for val in less:
            curr.val = val
            curr = curr.next
        for val in more:
            curr.val = val
            curr = curr.next
        return head