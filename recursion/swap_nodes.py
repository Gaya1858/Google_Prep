from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = head
        while head1 and head1.next:
            head1.val, head1.next.val = head1.next.val, head1.val
            head1 = head1.next.next
        return head


s =Solution()
t = ListNode(1)
t.next = ListNode(2)
t.next.next = ListNode(3)
t.next.next.next = ListNode(4)
t.next.next.next.next = ListNode(5)

d = s.swapPairs(t)
while d:
    print(d.val)
    d =d.next
