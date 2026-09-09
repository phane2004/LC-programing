# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        li = []
        curr = head
        while curr != None:
            temp = []
            n = k
            while n > 0 and curr != None:
                temp.append(curr.val)
                curr = curr.next
                n -= 1
            if len(temp) == k:
                li.extend(temp[::-1])
            else:
                li.extend(temp)
        curr = head
        idx = 0
        while curr != None:
            curr.val = li[idx]
            curr = curr.next
            idx += 1
        return head