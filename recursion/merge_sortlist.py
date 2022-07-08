from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 is None:
        #     return list2
        # elif list2 is None:
        #     return list1
        #
        # elif list1.val < list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1,list2.next)
        #     return list2
        newHead = ListNode(-1)
        head = newHead
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = list1 if list1 is not None else list2
        return newHead.next



s =Solution()
t = ListNode(1)
t.next = ListNode(2)
t.next.next = ListNode(4)
t1 = ListNode(1)
t1.next = ListNode(3)
t1.next.next = ListNode(4)
d = s.mergeTwoLists(t,t1)
while d:
    print(d.val)
    d =d.next
