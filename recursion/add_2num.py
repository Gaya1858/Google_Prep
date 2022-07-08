# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        s = l1.val + l2.val
        if s < 10:
            ansNode = ListNode(s)
            ansNode.next = self.addTwoNumbers(l1.next, l2.next)
            return ansNode
        else:
            remainder = l1.val + l2.val - 10
            ansNode = ListNode(remainder)
            ansNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next,l2.next))
            return ansNode




s =Solution()
t = ListNode(2)
t.next = ListNode(4)
t.next.next = ListNode(3)
t1 = ListNode(5)
t1.next = ListNode(6)
t1.next.next = ListNode(4)
d =s.addTwoNumbers(t,t1)
while d:
    print(d.val)
    d =d.next