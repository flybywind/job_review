# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head

        mid = last = head
        while last is not None:
            last = last.next
            if last is not None:
                last = last.next
            else:
                break
            mid = mid.next
        prev = mid
        mid = mid.next
        prev.next = None
        prev = None
        # reverse the second half as FILO stack
        while mid is not None:
            next = mid.next
            mid.next = prev
            prev = mid
            mid = next
        j = prev
        i = head
        # merge the two halves:
        while i is not None and j is not None:
            n1 = i.next
            n2 = j.next
            i.next = j
            j.next = n1
            i = n1
            j = n2        
        return head