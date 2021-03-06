import sys
sys.setrecursionlimit(50000)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + "->" + str(self.next)

    def print_range(self, end):
        if self == end:
            return "E"
        else:
            if self.next is None:
                return str(self.val) + "->N"
            else:
                return str(self.val) + "->" + self.next.print_range(end)


class Solution:
    def sortList(self, head):
        def _iter_in(head, end):
            if head == end or head is None or head.next is None:
                return
            if head.next.next == end:
                if head.val > head.next.val:
                    head.val, head.next.val = (head.next.val, head.val)
                return
            print "range:\t", head.print_range(end)
            p = head.val
            i = head.next
            # check if all equal to p
            while i != end and i.val == p:
                i = i.next
            if i == end:
                return
            prev = head
            i = head.next
            j = None
            while True:
                while i != end and i.val <= p:
                    prev = i
                    i = i.next
                if i == end:
                    break

                if j is None:
                    j = i.next
                else:
                    j = j.next
                while j != end and j.val > p:
                    j = j.next

                if j == end:
                    break
                else:
                    i.val, j.val = (j.val, i.val)
            prev.val, head.val = (head.val, prev.val)

            _iter_in(head, prev)
            _iter_in(i, end)

        _iter_in(head, None)
        return head

s = Solution()
l = [1, 2, 3, 5, 2, 6, 9, 2, 1, 4, 1, 2]
# l = [2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2]
print len(l)
head = ListNode(l[0])
N = len(l)
node = head
for i in range(1, N):
    node.next = ListNode(l[i])
    node = node.next

s.sortList(head)
print "sort:\t", head