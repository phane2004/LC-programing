# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        curr = head
        while curr != None:
            l.append(curr.val)
            curr = curr.next
        curr = head
        left = 0
        right = len(l) - 1
        lf = True
        rf = False
        #print(l)
        while left <= right:
            if lf:
                curr.val = l[left]
                lf = False
                rf = True
                left += 1
            elif rf:
                curr.val = l[right]
                rf = False
                lf = True
                right -= 1
            curr = curr.next
        