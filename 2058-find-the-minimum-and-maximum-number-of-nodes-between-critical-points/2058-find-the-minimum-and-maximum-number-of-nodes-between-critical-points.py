# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head.next.next == None:
            return [-1, -1]
        l = []
        p_val = head.val
        curr = head.next

        idx = 1
        while curr.next != None:
            c_val = curr.val
            t = curr.next.val
            #print(p_val, c_val, t)
            if p_val > c_val < t or p_val < c_val > t:
                l.append(idx)
            p_val = curr.val
            curr = curr.next
            idx += 1
        length = len(l)
        #print(l)
        if length == 0 or length == 1:
            return [-1, -1]
        # elif length == 1:
        #     return [0, 0]
        else:
            minima = float('inf')
            for i in range(1, length):
                minima = min(minima, (l[i] - l[i - 1]))
            maxima = l[-1] - l[0]
            return [minima, maxima]
        